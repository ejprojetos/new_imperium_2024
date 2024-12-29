from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Admin, Role, User, Doctor, Patient, Receptionist

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class AdminSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)  # Display roles as objects
    first_name = serializers.CharField(source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name', required=True)
    email = serializers.EmailField(source='user.email', required=True)
    cpf = serializers.CharField(source='user.cpf', required=True)
    date_birth = serializers.DateField(source='user.date_birth', required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        fields = [
            'id', 'first_name', 'last_name', 'email', 'cpf', 
            'date_birth', 'password', 'roles'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        """Ensure the email is unique among Admins."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        """Create a new Admin instance with a related User."""
        user_data = {
            'first_name': validated_data["user"].pop('first_name'),
            'last_name': validated_data["user"].pop('last_name'),
            'email': validated_data["user"].pop('email'),
            'cpf': validated_data["user"].pop('cpf'),
            'date_birth': validated_data["user"].pop('date_birth'),
            'password': validated_data.pop('password')
        }
        
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        
        admin = Admin.objects.create(user=user, **validated_data["user"])

        role, created = Role.objects.get_or_create(name='Admin', defaults={'description': 'Admin role'})
        user.roles.add(role)

        user.save()
        admin.save()
        
        return admin


class DoctorSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)  # Display roles as objects
    first_name = serializers.CharField(source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name', required=True)
    email = serializers.EmailField(source='user.email', required=True)
    cpf = serializers.CharField(source='user.cpf', required=True)
    date_birth = serializers.DateField(source='user.date_birth', required=True)
    password = serializers.CharField(write_only=True, required=True)
    specialty = serializers.CharField(required=True)
    #clinic = serializers.CharField(source='user.clinic', required=True)  # Add clinic field

    class Meta:
        model = Doctor
        fields = [
            'id', 'first_name', 'last_name', 'email', 'cpf', 
            'date_birth', 'password', 'roles', 'specialty', #'clinic'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        """Ensure the email is unique among Doctors."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        """Create a new Doctor instance with a related User."""
        user_data = {
            'first_name': validated_data["user"].pop('first_name'),
            'last_name': validated_data["user"].pop('last_name'),
            'email': validated_data["user"].pop('email'),
            'cpf': validated_data["user"].pop('cpf'),
            'date_birth': validated_data["user"].pop('date_birth'),
            'password': validated_data.pop('password'),
            #'clinic': validated_data["user"].pop('clinic')  # Add clinic to user data
        }
        
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        
        doctor = Doctor.objects.create(user=user, specialty=validated_data.pop('specialty'), **validated_data["user"])

        role, created = Role.objects.get_or_create(name='Doctor', defaults={'description': 'Doctor role'})
        user.roles.add(role)

        user.save()
        doctor.save()
        
        return doctor
    
class PatientSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)  # Display roles as objects
    first_name = serializers.CharField(source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name', required=True)
    email = serializers.EmailField(source='user.email', required=True)
    cpf = serializers.CharField(source='user.cpf', required=True)
    date_birth = serializers.DateField(source='user.date_birth', required=True)
    password = serializers.CharField(write_only=True, required=True)
    #medical_record_number = serializers.CharField(required=True)

    class Meta:
        model = Patient
        fields = [
            'id', 'first_name', 'last_name', 'email', 'cpf', 
            'date_birth', 'password', 'roles', #'medical_record_number'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        """Ensure the email is unique among Patients."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        """Create a new Patient instance with a related User."""
        user_data = {
            'first_name': validated_data["user"].pop('first_name'),
            'last_name': validated_data["user"].pop('last_name'),
            'email': validated_data["user"].pop('email'),
            'cpf': validated_data["user"].pop('cpf'),
            'date_birth': validated_data["user"].pop('date_birth'),
            'password': validated_data.pop('password')
        }
        
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        
        #patient = Patient.objects.create(user=user, medical_record_number=validated_data.pop('medical_record_number'), **validated_data["user"])
        patient = Patient.objects.create(user=user, **validated_data["user"])

        role, created = Role.objects.get_or_create(name='Patient', defaults={'description': 'Patient role'})
        user.roles.add(role)

        user.save()
        patient.save()
        
        return patient


class ReceptionistSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)  # Display roles as objects
    first_name = serializers.CharField(source='user.first_name', required=True)
    last_name = serializers.CharField(source='user.last_name', required=True)
    email = serializers.EmailField(source='user.email', required=True)
    cpf = serializers.CharField(source='user.cpf', required=True)
    date_birth = serializers.DateField(source='user.date_birth', required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Receptionist
        fields = [
            'id', 'first_name', 'last_name', 'email', 'cpf', 
            'date_birth', 'password', 'roles'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        """Ensure the email is unique among Receptionists."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        """Create a new Receptionist instance with a related User."""
        user_data = {
            'first_name': validated_data["user"].pop('first_name'),
            'last_name': validated_data["user"].pop('last_name'),
            'email': validated_data["user"].pop('email'),
            'cpf': validated_data["user"].pop('cpf'),
            'date_birth': validated_data["user"].pop('date_birth'),
            'password': validated_data.pop('password')
        }
        
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        
        receptionist = Receptionist.objects.create(user=user, **validated_data["user"])

        role, created = Role.objects.get_or_create(name='Receptionist', defaults={'description': 'Receptionist role'})
        user.roles.add(role)

        user.save()
        receptionist.save()
        
        return receptionist


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Adicionar os papéis (roles) do usuário
        roles = self.user.roles.values_list('name', flat=True)
        data['user_role'] = list(roles)
        
        return data
