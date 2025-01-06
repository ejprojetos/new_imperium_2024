from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Role, User
from commom.models import Address
from clinic.models import Clinic


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
    
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    cpf = serializers.CharField(required=True)
    date_birth = serializers.DateField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'cpf', 'date_birth',
            'password', 'roles', 'address', 'clinics'
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
