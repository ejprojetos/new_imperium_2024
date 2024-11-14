from rest_framework import serializers
from .models import MedicalRecord, Appointment, Room, Notification
from users.models import Patient, Doctor
from .models import WaitingList, WorkingHours
from django.utils import timezone
from datetime import datetime


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