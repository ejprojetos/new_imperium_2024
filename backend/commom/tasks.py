# Create your tasks her
from celery import shared_task
from .validators import validar_email
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

@shared_task
def send_email(data):
    try:
        recipient_email = validar_email(data["recipient_email"])
        subject = data["subject"]
        message = data["message"]
        send_mail(subject, message, None, [recipient_email])
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
