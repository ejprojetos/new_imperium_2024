from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import Role, User
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
    