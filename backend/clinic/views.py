from rest_framework import viewsets, status, permissions, filters

from rest_framework.response import Response 
from .models import MedicalRecord, Appointment, Room, Clinic, Notification, Clinic, WaitingList, WorkingHours, Clinic
from .serializers import MedicalRecordSerializer, RoomSerializer, NotificationSerializer, AssignDoctorSerializer, WaitingListSerializer, WorkingHoursSerializer, AppointmentSerializer, ClinicSerializer
from users.permissions import IsRoleUser
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from .pagination import SmallPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from users.models import User
from .tasks import send_notifications
from datetime import datetime, timedelta

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['address__city', 'address__neighborhood', 'address__zip_code']
    search_fields = ['name', 'cnpj', 'email_responsavel', 'cpf_responsavel', 'nome_responsavel', 'rg_responsavel', 'telefone_responsavel']
    lookup_field = 'id'
    lookup_url_kwarg = 'clinic_id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(admins_clinic=user)

class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
        The `MedicalRecordViewSet` allows doctors and administrators to view, create medical records. 
        Only users with the role of doctor or administrator can access this view: doctors can create new records, 
        while both doctors and administrators can update existing records and view all records.
    """

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    required_roles = ['DOCTOR','ADMIN']
    permission_classes = [IsRoleUser]
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        appointment_id = self.kwargs.get('appointment_id')
        if appointment_id is not None:
            return MedicalRecord.objects.filter(appointment_id=appointment_id).order_by('id')

        return super().get_queryset()
        
    def list(self, request, *args, **kwargs):
        appointment_id = self.kwargs.get('appointment_id')
        appointment = Appointment.objects.filter(id=appointment_id).exists()

        if appointment:
            return super().list(request, *args, **kwargs)
        else:
            return Response({'detail': 'appointment not exist'}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            appointment = serializer.validated_data.get('appointment')

            if MedicalRecord.objects.filter(appointment__id=appointment.id).exists():
                return Response({"detail": "it is not possible to create a medical record with the same appointment"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    required_roles = ['RECEPTIONIST', 'ADMIN']
    permission_classes = [IsRoleUser]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    lookup_field = 'uuid'  # Define o campo de busca como 'uuid'

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        clinic_id = self.kwargs['clinic_id']
        return Room.objects.filter(clinic_id=clinic_id)

    def create(self, request, *args, **kwargs):
        clinic_id = self.kwargs['clinic_id']
        clinic = get_object_or_404(Clinic, id=clinic_id)
        
        serializer = self.get_serializer(data=request.data, context={'clinic': clinic})
        if serializer.is_valid():
            serializer.save(clinic=clinic)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        clinic_id = self.kwargs['clinic_id']
        clinic = get_object_or_404(Clinic, id=clinic_id)

        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'clinic': clinic})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class NotificationViewSet(viewsets.ModelViewSet):
    """
        The `NotificationViewSet` allows users to view, update and delete their notifications. 
        Users can retrieve a list of notifications, filter them by type, read status, and date, 
        and manage the status of each notification (marking them as read or unread).
    """

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get','put','delete']
    pagination_class = SmallPagination # difinindo uma paginação de 5 elementos por pagina
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['type','datetime', 'is_read']   
    ordering_fields = ('datetime',)
    lookup_field = 'pk'

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id is not None:
            return Notification.objects.filter(user_id=user_id).order_by('id')
        else:
            return super().get_queryset()

    def list(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        user = User.objects.filter(id=user_id).exists()

        if user:
            return super().list(request, *args, **kwargs)
        else:
            return Response({'detail': 'user not exist'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        notification_pk = self.kwargs.get('pk')
        if notification_pk is not None:
            notification = Notification.objects.filter(pk=notification_pk).first()
            if notification:
                serializer = self.get_serializer(notification)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        notification_pk = self.kwargs.get('pk')
        notification = Notification.objects.filter(pk=notification_pk).first()
        if not notification:
            return Response({'detail': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(notification, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        is_read_req = serializer.validated_data.get('status')
        if is_read_req == 'accept':
            # create notification for confirmation
            #send_notifications.delay(users=[notification.user.id],type_notification="info", subtype_notification='confirmation')
            pass
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def destroy(self, request, *args, **kwargs):
        notification_id = self.kwargs['pk']
        notification = Notification.objects.get(id=notification_id)
        self.perform_destroy(notification)

        return Response({'detail': 'notification deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

class WaitingListViewSet(viewsets.ModelViewSet):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer
    required_roles = ['RECEPTIONIST', 'DOCTOR']
    permission_classes = [IsRoleUser]
    http_method_names = ['post', 'delete', 'put']
    
    def get_serializer_class(self):
        # Usar AssignDoctorSerializer apenas para a ação assign_doctor
        if self.action == 'assign_doctor':
            return AssignDoctorSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        waiting_list_item = self.get_object()
        waiting_list_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['put'], url_path='assign-doctor')
    def assign_doctor(self, request, pk=None):
        waiting_list = self.get_object()  # Obtém a instância da lista de espera
        serializer = AssignDoctorSerializer(data=request.data, context={'waiting_list': waiting_list})

        if serializer.is_valid():
            doctor_id = serializer.validated_data['doctor_id']
            waiting_list.doctor_id = doctor_id
            waiting_list.status = "in_progress"
            waiting_list.save()
            return Response({"detail": "Doctor assigned successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkingHoursViewSet(viewsets.ModelViewSet):
    queryset = WorkingHours.objects.all()
    serializer_class = WorkingHoursSerializer
    required_roles = ['DOCTOR']
    permission_classes = [IsRoleUser]
    http_method_names = ['get', 'post', 'delete', 'put']

    def get_queryset(self):
        """
        Return a list of working hours for the authenticated user.
        """
        return WorkingHours.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Create a new working hours for the authenticated user.
        """
        if not serializer.validated_data.get('user'):
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['status', 'appointment_date', 'clinic__name']
    search_fields = ['patient__first_name', 'doctor__first_name', 'reason', 'room__number']
    lookup_field = 'uuid'
    http_method_names = ['get', 'post', 'delete', 'put']
    pagination_class = SmallPagination

    def get_queryset(self):
        queryset = Appointment.objects.all()

        #filtrar pelo dia atual
        if self.request.query_params.get('today'):
            queryset = queryset.filter(appointment_date__date=datetime.now().date())

        #filtrar pelo dia seguinte - amanha
        if self.request.query_params.get('tomorrow'):
            queryset = queryset.filter(appointment_date__date=datetime.now().date() + timedelta(days=1))

        #filtrar pelos dias da semana
        dia = self.request.query_params.get('day')
        if dia:
            dict_dias = {
                'domingo': 1,
                'segunda': 2,
                'terca': 3,
                'quarta': 4,
                'quinta': 5,
                'sexta': 6,
                'sabado': 7
            }
            dia = dict_dias.get(dia)
            queryset = queryset.filter(appointment_date__date__week_day=dia)

        #filtro por mes
        mes = self.request.query_params.get('month')
        if mes:
            dict_mes = {
                'janeiro': 1,
                'fevereiro': 2,
                'marco': 3,
                'abril': 4,
                'maio': 5,
                'junho': 6,
                'julho': 7,
                'agosto': 8,
                'setembro': 9,
                'outubro': 10,
                'novembro': 11,
                'dezembro': 12
            }
            mes = dict_mes.get(mes)
            queryset = queryset.filter(appointment_date__month=mes)
            
        return queryset
    
    def validate_appointment(self, patient, doctor, appointment_date):
        """
        Comprehensive validation for appointment creation/update
        """
        # Check doctor's availability
        day_of_week = appointment_date.weekday() + 1  # Django model uses 1-7

        #checkando se os usuarios possuem o usuario correto
        if not patient.roles.filter(name="PATIENT").exists():
            raise ValidationError("ID definido não corresponde a um usuário PATIENT.")
        
        elif not doctor.roles.filter(name="DOCTOR").exists():
            raise ValidationError("ID definido não corresponde a um usuário DOCTOR.")
        else:
            try:
                # Check working hours
                working_hours = WorkingHours.objects.filter(
                        user=doctor, 
                        day_of_week=day_of_week
                    )

                not_available = True
                    
                for working_hour in working_hours:
                    # Validate appointment time is within working hours
                    if (working_hour.start_time <= appointment_date.time() <= working_hour.end_time):
                        not_available = False
                        break
                        
                if not_available:
                    raise ValidationError(f"Doctor is not available at the selected time.")
            
            except WorkingHours.DoesNotExist:
                raise ValidationError("Doctor does not have defined working hours for this day")
            
        # Check for existing appointments
        conflicting_appointments = Appointment.objects.filter(
            doctor=doctor,
            appointment_date__date=appointment_date.date(),
            status__in=['scheduled', 'in_progress']
        )
        
        # Check for time conflicts (1-hour buffer)
        for appt in conflicting_appointments:
            if abs((appt.appointment_date - appointment_date).total_seconds()) < 3600:
                raise ValidationError("Doctor has a conflicting appointment")
        
        # Check patient's appointment conflicts
        patient_conflicts = Appointment.objects.filter(
            patient=patient,
            appointment_date__date=appointment_date.date(),
            status__in=['scheduled', 'in_progress']
        )
        
        if patient_conflicts.exists():
            raise ValidationError("Patient has a conflicting appointment")
    
    def create(self, request, *args, **kwargs):
        """
        Custom create method with additional validation
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            # Extract validated data
            patient = serializer.validated_data['patient']
            doctor = serializer.validated_data['doctor']
            appointment_date = serializer.validated_data['appointment_date']
            clinic = serializer.validated_data['clinic']
            reason = serializer.validated_data['reason']
            room = serializer.validated_data.get('room')
            
            # Validate appointment
            self.validate_appointment(patient, doctor, appointment_date)
            
            # Create appointment
            appointment = Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                clinic=clinic,
                appointment_date=appointment_date,
                reason=reason,
                room=room
            )

            #notification for patient accept appointment
            #send_notifications.delay(users=[patient.user.id],type_notification="alert", subtype_notification='confirmation_appointment', flag_email=True)

            #notification for Room assignment logic for consultation
            #send_notifications.delay(users=[patient.user.id, doctor.user.id],type_notification="info", subtype_notification='room', room=room.number)
            return Response(
                self.get_serializer(appointment).data, 
                status=status.HTTP_201_CREATED
            )
        
        except ValidationError as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def update(self, request, *args, **kwargs):
        """
        Custom update method with availability checks
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Check if appointment can be updated
        if instance.status == 'completed':
            return Response(
                {'error': 'Completed appointments cannot be modified'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(
            instance, 
            data=request.data, 
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        
        try:
            # Extract validated data
            patient = serializer.validated_data.get('patient', instance.patient)
            doctor = serializer.validated_data.get('doctor', instance.doctor)
            appointment_date = serializer.validated_data.get('appointment_date', instance.appointment_date)
            
            # Validate appointment
            self.validate_appointment(patient, doctor, appointment_date)
            
            # Perform update
            self.perform_update(serializer)
            return Response(serializer.data)
        
        except ValidationError as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, uuid=None):
        """
        Custom action to cancel an appointment
        """
        appointment = self.get_object()
        
        # Check if appointment is already completed or canceled
        if appointment.status in ['completed', 'canceled']:
            return Response(
                {'error': 'Appointment cannot be canceled'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Update status to canceled
        appointment.status = 'canceled'
        appointment.save()

        # create notification for canceled appointment
        #send_notifications.delay(users=[appointment.doctor.user.id, appointment.patient.user.id], type_notification="info", subtype_notification='canceled')

        return Response(
            AppointmentSerializer(appointment).data, 
            status=status.HTTP_200_OK
        )
