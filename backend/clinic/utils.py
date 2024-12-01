from commom.tasks import send_email
from .serializers import NotificationSerializer

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
    
    messages = {
        'info': {
            'confirmation': {
                'patient': (
                    f"Olá {appointment.patient.user.first_name}! Sua consulta está confirmada: \n"
                    f"Doutor: {appointment.doctor.user.first_name},\n"
                    f"Sala: {appointment.room.number},\n"
                    f"Data: {appointment.appointment_date}.\n"
                    f"Se precisar de mais informações, entre em contato conosco."
                ),
                'doctor': (
                    f"Olá Dr(a). {appointment.doctor.user.first_name}! Sua consulta está confirmada com o paciente "
                    f"{appointment.patient.user.first_name} na sala {appointment.room.number} no dia {appointment.appointment_date}."
                )
            },
            'canceled': {
                'patient': (
                    f"Olá {appointment.patient.user.first_name}! Informamos que sua consulta com o Dr(a). "
                    f"{appointment.doctor.user.first_name} marcada para a sala {appointment.room.number} no dia "
                    f"{appointment.appointment_date} foi cancelada.\n"
                    f"Se desejar, entre em contato conosco para reagendar."
                ),
                'doctor': (
                    f"Olá Dr(a). {appointment.doctor.user.first_name}! Informamos que a consulta com o paciente "
                    f"{appointment.patient.user.first_name} marcada para a sala {appointment.room.number} no dia "
                    f"{appointment.appointment_date} foi cancelada.\n"
                    f"Entre em contato para mais informações, se necessário."
                )
            }
        },
        'warning': {
            'reschedule': {
                'patient': (
                    f"Olá {appointment.patient.user.first_name}! Informamos que sua consulta precisou ser reagendada para: \n"
                    f"Doutor: {appointment.doctor.user.first_name},\n"
                    f"Sala: {appointment.room.number},\n"
                    f"Nova data: {appointment.appointment_date}."
                ),
                'doctor': (
                    f"Olá Dr(a). {appointment.doctor.user.first_name}! Informamos que a consulta com o paciente "
                    f"{appointment.patient.user.first_name} foi reagendada para a sala {appointment.room.number} no dia {appointment.appointment_date}."
                )
            }
        },
        'alert': {
            'confirmation': {
                'patient': (
                    f"Olá {appointment.patient.user.first_name}!\n"
                    f"Precisamos da sua confirmação para a seguinte consulta:\n"
                    f"Doutor: {appointment.doctor.user.first_name},\n"
                    f"Sala: {appointment.room.number},\n"
                    f"Data: {appointment.appointment_date}.\n"
                    f"Por favor, confirme o mais rápido possível."
                ),
                'doctor': (
                    f"Olá Dr(a). {appointment.doctor.user.first_name}!\n"
                    f"Estamos aguardando a confirmação do paciente {appointment.patient.user.first_name} para a consulta: \n"
                    f"sala {appointment.room.number}\ndia {appointment.appointment_date}."
                )
            }
        },
        'reminder': {
            'appointment': {
                'patient': (
                    f"Olá {appointment.patient.user.first_name}! Esse é um lembrete para a sua consulta:\n"
                    f"Doutor: {appointment.doctor.user.first_name},\n"
                    f"Sala: {appointment.room.number},\n"
                    f"Data: {appointment.appointment_date}.\n"
                    f"Por favor, chegue com 15 minutos de antecedência."
                ),
                'doctor': (
                    f"Olá Dr(a). {appointment.doctor.user.first_name}! Esse é um lembrete para sua consulta com o paciente "
                    f"{appointment.patient.user.first_name} na sala {appointment.room.number} no dia {appointment.appointment_date}."
                )
            }
        }
    }
    
    data_notification = {
        'type': type_notification,
        'user': appointment.patient.user.id,
    }

    
    if type_user == 'patient':
        data_notification['message'] = messages[type_notification][subtype_notification]['patient']
    else:
        data_notification['message'] = messages[type_notification][subtype_notification]['doctor']

    return data_notification

def save_notification_and_send_email(user, data_notification):
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
        #send notifications
        data_email = {
            'recipient_email': user.user.email,
            'subject': 'NOTIFICAÇÃO DE CONSULTA',
            'message': data_notification["message"]
        }
        print(data_email)
        send_email.delay(data_email)

def send_notifications(type_notification, subtype_notification, appointment):
    """
        base function to call the helper functions 'generate_notification_data' and 'save_notification_and_send_email'

        - kwargs: 
            - type_notification, 
            - subtype_notification
            - appointment
        
        - return: None
    """

    #create notification for patient
    data_notification_patient = generate_notification_data(type_notification, subtype_notification, appointment, type_user='patient')
    #print(data_notification_patient)
    save_notification_and_send_email(appointment.patient, data_notification_patient)
    #create notification for doctor
    data_notification_doctor = generate_notification_data(type_notification, subtype_notification, appointment,type_user='doctor')
    save_notification_and_send_email(appointment.doctor, data_notification_doctor)