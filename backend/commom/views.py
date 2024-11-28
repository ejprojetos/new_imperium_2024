from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
#from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema, OpenApiResponse
#from .validators import validar_email
from .tasks import send_email

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
        data = request.data
        send_email.delay(data)
        return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)