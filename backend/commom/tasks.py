# Create your tasks her
from celery import shared_task
from .validators import validar_email
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from clinic.serializers import NotificationSerializer
from users.models import User

@shared_task
def send_email(data):
    try:
        recipient_email = validar_email(data["recipient_email"])
        subject = data["subject"]
        message = data["message"]
        send_mail(subject, message, None, [recipient_email])
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@shared_task
def send_notifications(users, type_notification, subtype_notification, flag_email=False):
    """
        base function to call the helper functions 'generate_notification_data' and 'save_notification_and_send_email'

        - kwargs: 
            - users: users for create notifications
            - type_notification, 
            - subtype_notification
            - appointment
            - flag_email: true -> send email, false -> not send email
        
        - return: None
    """

    messages = {
        'info': {
            'confirmation': 'solicitação aceita pelo paciente!',
            'canceled': 'consulta cancelada com sucesso!',
        },
        'warning': {
            
        },
        'alert': {
            'confirmation': 'você precisa confirmar sua consulta!'
        },
        'reminder': {
            
        }
    }

    for user_id in users:
        user = User.objects.get(id=user_id)
        data_notification = {
            'type': type_notification,
            'user': user.id,
            'message': messages[type_notification][subtype_notification]
        }

        data_notification_serial = NotificationSerializer(data=data_notification)
        if data_notification_serial.is_valid(raise_exception=True):
            data_notification_serial.save()
            if flag_email:
                #send notifications
                data_email = {
                    'recipient_email': user.email,
                    'subject': 'NOTIFICAÇÃO DE CONSULTA',
                    'message': data_notification["message"]
                }
                send_email.delay(data_email)