from rest_framework import serializers
from .models import MedicalRecord, Appointment, Room, Notification
from users.models import Patient, Doctor
from .models import WaitingList, WorkingHours
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.ReadOnlyField(source='appointment.patient.id')
    doctor = serializers.ReadOnlyField(source='appointment.doctor.id')
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = MedicalRecord
        fields = ['uuid', 'patient', 'doctor', 'appointment', 'allergies', 'issues', 'medication', 'anamnesis', 'new_medication', 'exams']
        read_only_fields = ['uuid']



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['uuid', 'clinic', 'number', 'description']
        extra_kwargs = {
            'clinic': {'read_only': True}  # O ID da clínica será passado pela URL, não pelo corpo da requisição
        }

    def validate_number(self, value):
        clinic = self.context['clinic']
        room_id = self.instance.id if self.instance else None
        
        # Verifica se há outra sala com o mesmo número na clínica, ignorando a sala atual
        if Room.objects.filter(clinic=clinic, number=value).exclude(id=room_id).exists():
            raise serializers.ValidationError("A room with this number already exists in this clinic.")
        
        return value
    
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'is_read', 'type', 'datetime', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }


class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = ['patient', 'clinic', 'arrival_datetime', 'status', 'doctor']
        
    def validate(self, data):
        # Validação para verificar se o paciente já está na fila da mesma clínica
        patient = data.get('patient')
        clinic = data.get('clinic')
        
        if WaitingList.objects.filter(patient=patient, clinic=clinic, status='waiting').exists():
            raise serializers.ValidationError("The patient is already in the waiting list.")
        
        # Validação para checar se a clínica está ativa e com médicos disponíveis (opcional)
        if not clinic.is_active:
            raise serializers.ValidationError("The clinic is not active.")
        
        # Verificar horário de funcionamento do médico (opcional)
        doctor = data.get('doctor')
        if doctor:
            current_day = timezone.now().isoweekday()
            current_time = timezone.now().time()
            working_hours = WorkingHours.objects.filter(
                user=doctor.user, day_of_week=current_day,
                start_time__lte=current_time, end_time__gte=current_time
            )
            if not working_hours.exists():
                raise serializers.ValidationError("The doctor is not available at the moment.")
        
        return data


class AssignDoctorSerializer(serializers.Serializer):
    class Meta:
        model = WaitingList
        fields = ['doctor']

    doctor_id = serializers.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Popula o campo doctor_id com opções de médicos disponíveis
        self.fields['doctor_id'].choices = [
            (doctor.id, f"{doctor.user.first_name} {doctor.user.last_name}")
            for doctor in Doctor.objects.all()
        ]

    def validate_doctor_id(self, doctor_id):
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            raise serializers.ValidationError("The specified doctor does not exist.")

        # Verifica se o médico está disponível (validação de horários de trabalho)
        current_day = timezone.now().isoweekday()
        current_time = timezone.now().time()
        working_hours = WorkingHours.objects.filter(
            user=doctor.user, 
            day_of_week=current_day,
            start_time__lte=current_time, 
            end_time__gte=current_time
        )
        if not working_hours.exists():
            raise serializers.ValidationError("The doctor is not available at the moment.")

        return doctor_id

    def validate(self, data):
        waiting_list = self.context['waiting_list']
        
        # Verifica se o paciente está com status "waiting"
        if waiting_list.status != "waiting":
            raise serializers.ValidationError("The patient is not currently waiting.")
        
        return data


class WorkingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingHours
        fields = ['user', 'day_of_week', 'start_time', 'end_time']

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        user_data = data.get('user')
        print(user_data)

        # Garantir que end_time seja posterior a start_time
        if start_time >= end_time:
            raise serializers.ValidationError("End time must be later than start time.")

        # Pegar o usuário autenticado se 'user' não está em data
        user = data.get('user') if 'user' in data else self.context['request'].user
        day_of_week = data.get('day_of_week')

        # Obter todos os horários existentes para o mesmo dia e usuário que se sobreponham ao novo horário
        conflicting_hours = WorkingHours.objects.filter(
            user=user,
            day_of_week=day_of_week,
            start_time__lt=end_time,   # Início antes do término do novo horário
            end_time__gt=start_time    # Término depois do início do novo horário
        )
        
        # Ignorar o horário atual (em caso de atualização)
        if self.instance:
            conflicting_hours = conflicting_hours.exclude(id=self.instance.id)

        # Verificação final de conflito
        if conflicting_hours.exists():
            raise serializers.ValidationError("There is a conflict with existing working hours.")

        return data


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['uuid', 'patient', 'doctor', 'clinic', 'appointment_date', 'reason', 'status', 'room']
        read_only_fields = ['uuid', 'status']
    
    def validate_appointment_date(self, value):
        """
        Validate that the appointment is scheduled for a future date
        """
        if value <= timezone.now():
            raise serializers.ValidationError("Appointment must be scheduled for a future date")
        return value
    
    def validate(self, data):
        """
        Comprehensive validation for appointment creation/update
        """
        # Get the relevant fields, using existing data if not being updated
        clinic = data.get('clinic', self.instance.clinic if self.instance else None)
        patient = data.get('patient', self.instance.patient if self.instance else None)
        doctor = data.get('doctor', self.instance.doctor if self.instance else None)
        appointment_date = data.get('appointment_date', self.instance.appointment_date if self.instance else None)
        room = data.get('room', self.instance.room if self.instance else None)
        
        # Check doctor's availability
        if doctor and appointment_date:
            day_of_week = appointment_date.weekday() + 1
            
            try:
                # Check working hours
                working_hours = WorkingHours.objects.get(
                    user=doctor.user, 
                    day_of_week=day_of_week
                )
                
                # Validate appointment time is within working hours
                if not (working_hours.start_time <= appointment_date.time() <= working_hours.end_time):
                    raise serializers.ValidationError(f"Doctor is not available at the selected time. Working hours are {working_hours.start_time} to {working_hours.end_time}")
                
            except WorkingHours.DoesNotExist:
                raise serializers.ValidationError("Doctor does not have defined working hours for this day")
            
            # Check for existing appointments
            conflicting_appointments = Appointment.objects.filter(
                doctor=doctor,
                appointment_date__date=appointment_date.date(),
                status__in=['scheduled', 'in_progress']
            )
            
            # Check for time conflicts (1-hour buffer)
            for appt in conflicting_appointments:
                if self.instance and appt.uuid == self.instance.uuid:
                    continue  # Skip current instance during update
                
                if abs((appt.appointment_date - appointment_date).total_seconds()) < 3600:
                    raise serializers.ValidationError("Doctor has a conflicting appointment")
        
        # Check patient's appointment conflicts
        if patient and appointment_date:
            patient_conflicts = Appointment.objects.filter(
                patient=patient,
                appointment_date__date=appointment_date.date(),
                status__in=['scheduled', 'in_progress']
            )
            
            # Exclude current instance during update
            if self.instance:
                patient_conflicts = patient_conflicts.exclude(uuid=self.instance.uuid)
            
            if patient_conflicts.exists():
                raise serializers.ValidationError("Patient has a conflicting appointment")
        
        # Try to assign a room automatically if none is specified
        if not room and clinic and appointment_date:
            try:
                room = self.assign_available_room(clinic, appointment_date)
                data['room'] = room
            except serializers.ValidationError:
                # Se não houver salas disponíveis, permite continuar sem sala
                data['room'] = None
        
        # If a specific room is provided, validate its availability
        elif room:
            self.validate_room_availability(room, appointment_date)   
        
        return data
    
    def assign_available_room(self, clinic, appointment_date):
        """
        Automatically assign an available room for the appointment.
        """
        # Calculate time range for conflict checking
        start_range = appointment_date - timedelta(hours=1)
        end_range = appointment_date + timedelta(hours=1)
        
        # Find conflicting appointments in the same clinic
        conflicting_appointments = Appointment.objects.filter(
            clinic=clinic,
            status__in=['scheduled', 'in_progress'],
            appointment_date__gte=start_range,
            appointment_date__lte=end_range
        )
        
        # Get all rooms in the clinic
        all_rooms = Room.objects.filter(clinic=clinic)
        
        # Find booked rooms during the time range
        booked_rooms = conflicting_appointments.values_list('room_id', flat=True)
        
        # Find available rooms
        available_rooms = all_rooms.exclude(id__in=booked_rooms)
        
        # If no rooms are available, raise an error
        if not available_rooms.exists():
            raise serializers.ValidationError("No rooms available for the appointment")
        
        # Count existing appointments for each available room
        room_appointment_counts = {}
        for room in available_rooms:
            room_appointment_counts[room.id] = Appointment.objects.filter(
                room=room, 
                clinic=clinic, 
                status__in=['scheduled', 'in_progress']
            ).count()
        
        # Select the room with the least number of existing appointments
        if room_appointment_counts:
            selected_room_id = min(room_appointment_counts, key=room_appointment_counts.get)
            return Room.objects.get(id=selected_room_id)
        
        # Fallback if no room is found
        raise serializers.ValidationError("Unable to assign a room")
    
    def validate_room_availability(self, room, appointment_date):
        """
        Validate that the selected room is available during the appointment time.
        """
        # Calculate time range for conflict checking
        start_range = appointment_date - timedelta(minutes=30)
        end_range = appointment_date + timedelta(minutes=30)
        
        # Check for conflicting appointments in the same room
        conflicting_appointments = Appointment.objects.filter(
            room=room,
            status__in=['scheduled', 'in_progress'],
            appointment_date__gte=start_range,
            appointment_date__lte=end_range
        )
        
        # Exclude current appointment during update
        if self.instance:
            conflicting_appointments = conflicting_appointments.exclude(uuid=self.instance.uuid)
        
        if conflicting_appointments.exists():
            raise serializers.ValidationError(f"Room {room.number} is not available at the selected time")
