from rest_framework import serializers
from .models import User, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description')


class UserWithRolesSerializer(serializers.ModelSerializer):
    user_roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_roles')
