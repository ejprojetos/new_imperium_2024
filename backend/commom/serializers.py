from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError



class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        """
        Verifica se o e-mail está associado a um usuário no sistema.
        """
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Usuário com este e-mail não foi encontrado.")
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)

    def validate(self, data):
        """
        Valida o token JWT e os dados recebidos.
        """
        try:
            # Valida o token JWT recebido
            decoded_token = AccessToken(data['token'])
            if decoded_token["token_type"] != "access":
                raise serializers.ValidationError("Token inválido ou do tipo errado.")
        except TokenError:
            raise serializers.ValidationError("Token inválido ou expirado.")
        return data