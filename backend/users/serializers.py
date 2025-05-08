from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import Role, User, Expedient, UserPolicies, FAQ, Tag, UserSupport, UserSupport
from commom.models import Address
from clinic.models import Clinic, WorkingHours
from drf_extra_fields.fields import Base64ImageField, Base64FileField
from .utils import PDFBase64File
from clinic.serializers import WorkingHoursSerializer
from datetime import time

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class SimplifiedExpedientSerializer(serializers.ModelSerializer):
   class Meta:
       model = Expedient
       fields = ['days_of_week', 'turns']

class ExpedientSerializer(serializers.ModelSerializer):
    days_dict = {
            "Segunda-feira": 1,
            "Terça-feira": 2,
            "Quarta-feira": 3,
            "Quinta-feira": 4,
            "Sexta-feira": 5,
            "Sábado": 6,
            "Domingo": 7
       }

    times = {
        "Matutino": [7, 12],
        "Vespertino": [13, 18],
        "Noturno": [18, 23],
    }

    class Meta:
       model = Expedient
       fields = ['id','days_of_week', 'turns']

    def create(self, validated_data):   
       days = validated_data.get('days_of_week')
       turns = validated_data.get('turns')
       
       user = self.context['user']

       for day in days:
           for turn in turns:
               #criar as working hours com base nos dias e turnos
               working_hours = WorkingHours(user=user, day_of_week=self.days_dict[day], start_time=time(self.times[turn][0],0), end_time=time(self.times[turn][1],0))
               working_hours.save()
               pass

       return super().create(validated_data)
    
    def update(self, instance, validated_data):
        # Obtém os valores atualizados ou mantém os existentes
        days = validated_data.get("days_of_week", instance.days_of_week)
        turns = validated_data.get("turns", instance.turns)

        # Obtém o usuário do contexto
        user = self.context.get("user")

        # Se "days_of_week" ou "turns" forem atualizados, recria os horários de trabalho
        if "days_of_week" in validated_data or "turns" in validated_data:
            WorkingHours.objects.filter(user=user).delete()

            for day in days:
                for turn in turns:
                    working_hours = WorkingHours(
                        user=user,
                        day_of_week=self.days_dict[day],  
                        start_time=time(self.times[turn][0], 0),
                        end_time=time(self.times[turn][1], 0)
                    )
                    working_hours.save()

        return super().update(instance, validated_data)

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    role = RoleSerializer(required=False)
    #clinics = serializers.PrimaryKeyRelatedField(queryset=Clinic.objects.all(), many=True, required=False)
    expedient = ExpedientSerializer(required=False)

    # first_name = serializers.CharField(required=True)
    # email = serializers.EmailField(required=True)
    # cpf = serializers.CharField(required=True)
    # date_birth = serializers.DateField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    attach_document = PDFBase64File(required=False, allow_null=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'email', 'cpf', 'date_birth',
            'password', 'role', 'address', 'clinic', 'gender',
            'formacao', 'crm', 'attach_document','image', 'phone', 'expedient', 'availableForShift', 'terms_accepted'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'attach_document': {'write_only': True},  # Forçar escrita
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        clinic = validated_data.pop('clinic', None)
        #roles_data = roles_data[0]['name']
        role_data = validated_data.pop('role', None)
        expedient_data = validated_data.pop('expedient', None)
        attach_document = validated_data.pop("attach_document", None)

        # Se o campo 'role' não for enviado, atribui o padrão
        if role_data is None:
            role_data = Role.objects.get(name='PATIENT')  # ou pelo id: Role.objects.get(id=1)
            validated_data['role'] = role_data
        else:
            role_data = Role.objects.get(name=role_data['name'])  # Busca as roles pelos nomes
            validated_data['role'] = role_data

        address = None
        if address_data:
            address = Address.objects.create(**address_data)

        user = User.objects.create(**validated_data, address=address)
        user.set_password(validated_data['password'])

        if "ADMIN" in role_data.name:
            user.is_staff = True

        if attach_document:
            user.attach_document = attach_document

        if expedient_data:
            expedient_serializer = ExpedientSerializer(data=expedient_data, context={'user': user})
            if expedient_serializer.is_valid(raise_exception=True):
                expedient = expedient_serializer.save()
                user.expedient = expedient

        if clinic:
            user.clinic = clinic
            
        user.save()

        return user
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        clinic = validated_data.pop('clinic', None)
        role_data = validated_data.pop('role', [])
        expedient_data = validated_data.pop('expedient', None)

        # Atualiza endereço
        if address_data:
            if instance.address:
                for key, value in address_data.items():
                    setattr(instance.address, key, value)
                instance.address.save()
            else:
                instance.address = Address.objects.create(**address_data)

        # Atualiza role
        if role_data:
            #role_names = [role['name'] for role in role_data]
            role = Role.objects.get(name=role_data['name'])
            instance.role = role
            if "ADMIN" in role_data['name']:
                instance.is_staff = True
            else:
                instance.is_staff = False

        if expedient_data:  # Se expedient foi enviado na requisição
            if instance.expedient:
                expedient_instance = instance.expedient  # Pega o expedient atual do usuário
                expedient_serializer = ExpedientSerializer(expedient_instance, data=expedient_data, partial=True, context={'user': instance})

                if expedient_serializer.is_valid():
                    expedient_serializer.save()
                else:
                    raise serializers.ValidationError(expedient_serializer.errors)
            else:
                # Cria um novo expedient caso o usuário ainda não tenha um
                expedient_serializer = ExpedientSerializer(data=expedient_data, context={'user': instance})
                if expedient_serializer.is_valid(raise_exception=True):
                    expedient = expedient_serializer.save()
                    instance.expedient = expedient
                    instance.save()

        # Atualiza clínicas
        if clinic:
            instance.clinic = clinic

        # Atualiza outros campos do usuário
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)  # Garante que a senha seja armazenada corretamente
            else:
                setattr(instance, key, value)

        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Acessa diretamente o nome do role
        data['user_role'] = self.user.role.name if self.user.role else None
        
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
        data['user_role'] = user.role.name

        return data
    
class RecepcionistSerializer(UserSerializer):
    #working_hours = WorkingHoursSerializer(many=True, required=False)
    expedient = SimplifiedExpedientSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'email', 'cpf', 'date_birth',
            'role', 'address', 'clinic', 'gender', 'attach_document', 'phone', 'expedient'
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class UserPoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPolicies
        fields = '__all__'

    def create(self, validated_data):
        profile = validated_data.get('profile')  # Obtém o profile do request

        # Verifica se já existe um UserPoliciesSupport para este profile
        if UserPolicies.objects.filter(profile=profile).exists():
            raise serializers.ValidationError({"profile": "Já existe uma politica para este profile."})

        # Cria UserPoliciesSupport com a nova policy
        user_policy_support = UserPolicies.objects.create(**validated_data)

        return user_policy_support
    
    def update(self, instance, validated_data):
        profile = validated_data.get('profile')

        if instance.profile != profile:
            raise serializers.ValidationError({"profile": f"Não é possivel obter mais de uma politica para uma mesma profile, atualize o profile vinculado ao id, profile = {instance.profile}"})
        else:
            instance = super().update(instance, validated_data)
            return instance

class FAQSerializer(serializers.ModelSerializer):
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = FAQ
        fields = ['id', 'title', 'questions', 'content', 'profile', 'tags']

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

class UserSupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSupport
        fields = ['id','title', 'profile', 'manual_archive']
    