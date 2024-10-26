from rest_framework import serializers
from .models import User, Role

class AdminClinicSerializer(serializers.ModelSerializer):
    """Serializer for registering an Admin Clinic user."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method to handle password hashing and user creation."""
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class DoctorRegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering a Doctor user."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method to handle password hashing and user creation."""
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class PacientRegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering a Pacient user."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method to handle password hashing and user creation."""
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class RecepcionistRegisterSerializer(serializers.ModelSerializer):
    """Serializer for registering a Recepcionist user."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method to handle password hashing and user creation."""
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
