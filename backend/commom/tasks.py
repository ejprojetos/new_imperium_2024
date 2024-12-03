# Create your tasks her
from celery import shared_task
from .validators import validar_email
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from clinic.serializers import NotificationSerializer
from users.models import Patient, Doctor
from clinic.models import Room

@shared_task
def send_email(data):
    try:
        recipient_email = validar_email(data["recipient_email"])
        subject = data["subject"]
        message = data["message"]
        send_mail(subject, message, None, [recipient_email])
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def generate_notification_data(type_notification, subtype_notification, appointment, type_user):
    """
        function to create the dictionary with the data necessary to create a new notification

        - kargs:
            - type_notification
            - subtype_notification
            - appointment 
            - type_user

        - return:
            - data_notification; 
    """

    patient = Patient.objects.get(id=appointment['patient'])
    doctor = Doctor.objects.get(id=appointment['doctor'])
    room = Room.objects.get(id=appointment['room'])
    
    messages = {
        'info': {
            'confirmation': {
                'patient': (
                    f"Olá {patient.user.first_name}! Sua consulta está confirmada: \n"
                    f"Doutor: {doctor.user.first_name},\n"
                    f"Sala: {room.number},\n"
                    f"Data: {appointment['appointment_date']}.\n"
                    f"Se precisar de mais informações, entre em contato conosco."
                ),
                'doctor': (
                    f"Olá Dr(a). {doctor.user.first_name}! Sua consulta está confirmada com o paciente "
                    f"{patient.user.first_name} na sala {room.number} no dia ."
                )
            },
            'canceled': {
                'patient': (
                    f"Olá {patient.user.first_name}! Informamos que sua consulta com o Dr(a). "
                    f"{doctor.user.first_name} marcada para a sala {room.number} no dia "
                    f"{appointment['appointment_date']} foi cancelada.\n"
                    f"Se desejar, entre em contato conosco para reagendar."
                ),
                'doctor': (
                    f"Olá Dr(a). {doctor.user.first_name}! Informamos que a consulta com o paciente "
                    f"{patient.user.first_name} marcada para a sala {room.number} no dia "
                    f"{appointment['appointment_date']} foi cancelada.\n"
                    f"Entre em contato para mais informações, se necessário."
                )
            },
            'assignment': {
                'patient': (
                    f"Olá {patient.user.first_name}! Sua consulta foi atribuída à sala {room.number}:\n"
                    f"Doutor: {doctor.user.first_name},\n"
                    f"Data: {appointment['appointment_date']}.\n"
                    f"Por favor, compareça ao local no horário marcado."
                ),
                'doctor': (
                    f"Olá Dr(a). {doctor.user.first_name}! A consulta com o paciente "
                    f"{patient.user.first_name} foi atribuída à sala {room.number}.\n"
                    f"Data: {appointment['appointment_date']}.\n"
                    f"Por favor, prepare-se para o atendimento."
                )
            }
        },
        'warning': {
            
        },
        'alert': {
            'confirmation': {
                'patient': (
                    f"Olá {patient.user.first_name}!\n"
                    f"Precisamos da sua confirmação para a seguinte consulta:\n"
                    f"Doutor: {doctor.user.first_name},\n"
                    f"Sala: {room.number},\n"
                    f"Data: {appointment['appointment_date']}.\n"
                    f"Por favor, confirme o mais rápido possível."
                ),
                'doctor': (
                    f"Olá Dr(a). {doctor.user.first_name}!\n"
                    f"Estamos aguardando a confirmação do paciente {patient.user.first_name} para a consulta: \n"
                    f"sala {room.number}\ndia {appointment['appointment_date']}."
                )
            }
        },
        'reminder': {
            
        }
    }
    
    data_notification = {
        'type': type_notification,
        'user': patient.user.id,
    }

    
    if type_user == 'patient':
        data_notification['message'] = messages[type_notification][subtype_notification]['patient']
    else:
        data_notification['message'] = messages[type_notification][subtype_notification]['doctor']

    return data_notification

def save_notification_and_send_email(user, data_notification, flag_email):
    """
        function to validate the notification data and create a new notification, in addition, it queues the sending of emails in the task queue.

        - args:
            - user: user to whom information should be obtained to send the email
            - data_notification: data for creating the notification

        - return: None
    """


    data_notification_serial = NotificationSerializer(data=data_notification)
    if data_notification_serial.is_valid(raise_exception=True):
        data_notification_serial.save()
        if flag_email:
            #send notifications
            data_email = {
                'recipient_email': user.user.email,
                'subject': 'NOTIFICAÇÃO DE CONSULTA',
                'message': data_notification["message"]
            }
            send_email.delay(data_email)

@shared_task
def send_notifications(type_notification, subtype_notification, appointment, flag_email):
    """
        base function to call the helper functions 'generate_notification_data' and 'save_notification_and_send_email'

        - kwargs: 
            - type_notification, 
            - subtype_notification
            - appointment
            - flag_email: true -> send email, false -> not send email
        
        - return: None
    """

    patient = Patient.objects.get(id=appointment['patient'])
    doctor = Doctor.objects.get(id=appointment['doctor'])

    #create notification for patient
    data_notification_patient = generate_notification_data(type_notification, subtype_notification, appointment, type_user='patient')
    #print(data_notification_patient)
    save_notification_and_send_email(patient, data_notification_patient, flag_email)
    #create notification for doctor
    data_notification_doctor = generate_notification_data(type_notification, subtype_notification, appointment,type_user='doctor')
    save_notification_and_send_email(doctor, data_notification_doctor, flag_email)