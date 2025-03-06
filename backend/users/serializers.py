from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import Role, User, Policies, FAQ, Tag, UserPoliciesSupport, OtherArchives
from commom.models import Address
from clinic.models import Clinic
from drf_extra_fields.fields import Base64ImageField, Base64FileField
from .utils import PDFBase64File
from clinic.serializers import WorkingHoursSerializer

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    roles = RoleSerializer(many=True, required=False)
    clinics = serializers.PrimaryKeyRelatedField(queryset=Clinic.objects.all(), many=True, required=False)
    
    # first_name = serializers.CharField(required=True)
    # email = serializers.EmailField(required=True)
    # cpf = serializers.CharField(required=True)
    # date_birth = serializers.DateField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    attach_document = PDFBase64File(required=False)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'email', 'cpf', 'date_birth',
            'password', 'roles', 'address', 'clinics', 'gender',
            'formacao', 'crm', 'attach_document', 'phone'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        clinics = validated_data.pop('clinics', [])
        roles_data = validated_data.pop('roles', [])
        roles_data = roles_data[0]['name']

        address = None
        if address_data:
            address = Address.objects.create(**address_data)

        user = User.objects.create(**validated_data, address=address)
        user.set_password(validated_data['password'])
        user.save()

        if clinics:
            user.clinics.set(clinics)

        if roles_data:
            roles = Role.objects.filter(name=roles_data)  # Busca as roles pelos nomes
            user.roles.set(roles)

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        roles = self.user.roles.values_list('name', flat=True)
        data['user_role'] = list(roles)
        
        return data


from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRefreshObtainPairSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Decodificar o token de atualização para obter os dados do usuário
        refresh = RefreshToken(attrs['refresh'])
        user_id = refresh['user_id']
        
        # Obter o usuário a partir do ID
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        # Recuperar as roles do usuário
        roles = user.roles.values_list('name', flat=True)
        data['user_role'] = list(roles)

        return data
    
class RecepcionistSerializer(UserSerializer):
    working_hours = WorkingHoursSerializer(many=True, required=False)
    
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'email', 'cpf', 'date_birth',
            'roles', 'address', 'clinics', 'gender', 'attach_document', 'working_hours', 'phone'
        ]

class OtherArchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherArchives
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = FAQ
        fields = ['title', 'questions', 'content', 'profile', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        faq = super().create(validated_data)

        if tags_data:
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(**tag_data)
                faq.tags.add(tag)

        return faq
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)  # Extrai as tags, se existirem
        instance = super().update(instance, validated_data)  # Atualiza os outros campos do FAQ

        if tags_data is not None:
            instance.tags.clear()  # Remove todas as tags associadas antes de atualizar
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(**tag_data)  # Obtém ou cria a tag
                instance.tags.add(tag)  # Associa a tag ao FAQ

        return instance

class UserPoliciesSupportSerializer(serializers.ModelSerializer):
    policy = PoliciesSerializer()
    other_files = OtherArchivesSerializer(required=False, many=True)

    class Meta:
        model = UserPoliciesSupport
        fields = ['id', 'profile', 'policy', 'manual_archive', 'other_files']

    def create(self, validated_data):
        policy_data = validated_data.pop('policy', None)
        profile = validated_data.get('profile')  # Obtém o profile do request

        # Verifica se já existe um UserPoliciesSupport para este profile
        if UserPoliciesSupport.objects.filter(profile=profile).exists():
            raise serializers.ValidationError({"profile": "Já existe um objeto UserPoliciesSupport para este profile."})

        if policy_data:  
            # Cria a policy antes de criar UserPoliciesSupport
            policy_instance = Policies.objects.create(**policy_data)
        else:
            raise serializers.ValidationError({"policy": "Este campo é obrigatório."})

        # Cria UserPoliciesSupport com a nova policy
        user_policy_support = UserPoliciesSupport.objects.create(policy=policy_instance, **validated_data)

        return user_policy_support
    
    def update(self, instance, validated_data):
        policy_data = validated_data.pop('policy', None)
        other_files_data = validated_data.pop('other_files', None)

        # Atualiza os outros campos do UserPoliciesSupport
        instance = super().update(instance, validated_data)

        if policy_data:
            # Atualiza os campos da policy existente
            for attr, value in policy_data.items():
                setattr(instance.policy, attr, value)
            instance.policy.save()

        if other_files_data is not None:
            # Atualiza os arquivos associados, removendo os antigos e adicionando os novos
            instance.other_files.clear()
            for file_data in other_files_data:
                file_instance = OtherArchives.objects.create(**file_data)
                instance.other_files.add(file_instance)

        return instance

    