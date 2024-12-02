from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.core.mail import send_mail
from django.urls import reverse
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .validators import validar_email
from users.models import User
from commom.serializers import PasswordResetRequestSerializer, PasswordResetConfirmSerializer


class EmailAPIView(APIView):
    """
        view for sending an email, passing the sender, recipient, subject and body of the email as parameters in the request
    """
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "recipient_email": {"type": "string", "example": "recipient@example.com"},
                    "subject": {"type": "string", "example": "example"},
                    "message": {"type": "string", "example": "example"},
                },
                "required": ["recipient_email", "subject"]
            }
        },
        responses={
            200: OpenApiResponse(
                description="Email sent successfully",
                response={
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "example": "Message sent successfully!"}
                    },
                }
            ),
        }
    )
    def post(self, request):
        try:
            data = request.data
            recipient_email = validar_email(data["recipient_email"])
            subject = data["subject"]
            message = data["message"]
            send_mail(subject, message, None, [recipient_email])
            return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetRequestView(GenericAPIView):
    """View for requesting a password reset."""
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        # Busca o usuário e gera o token JWT
        user = User.objects.get(email=email)
        refresh = RefreshToken.for_user(user)  # Gera Refresh Token
        access_token = refresh.access_token  # Gera Access Token

        # Obtém o JTI do token
        jti = access_token.get("jti")
        expires_at_timestamp = access_token['exp']  # Expiração do token (em segundos)
        expires_at = datetime.fromtimestamp(expires_at_timestamp)  # Converte para datetime

        # Remove qualquer token existente com o mesmo JTI
        OutstandingToken.objects.filter(jti=jti).delete()

        # Registra o token como outstanding (válido) no banco de dados
        OutstandingToken.objects.create(
            user=user,
            jti=jti,
            token=str(access_token),
            expires_at=expires_at,
        )

        # Monta o link de redefinição de senha
        reset_url = request.build_absolute_uri(
            reverse('password-reset-confirm')  # Nome da URL de redefinição
        )
        reset_url = f"{reset_url}?token={access_token}"

        # Envia o e-mail
        send_mail(
            "Redefinição de Senha",
            f"Use o link abaixo para redefinir sua senha:\n{reset_url}\nToken:\n{access_token}",
            None,
            [email],
        )

        return Response({"message": "E-mail de redefinição enviado com sucesso."}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(GenericAPIView):
    """
    View for confirming the password reset.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']

        try:
            # Decodifica o token
            decoded_token = AccessToken(token)
            user_id = decoded_token["user_id"]

            # Redefine a senha do usuário
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()

            # Busca o token outstanding
            outstanding_token = OutstandingToken.objects.get(token=token)

            # Move o token para a blacklist
            BlacklistedToken.objects.create(token=outstanding_token)

            return Response({"message": "Senha redefinida com sucesso."}, status=status.HTTP_200_OK)

        except TokenError:
            return Response({"message": "Token inválido ou expirado."}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except OutstandingToken.DoesNotExist:
            return Response({"message": "Token não encontrado na lista de tokens válidos."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"Erro ao invalidar o token: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
