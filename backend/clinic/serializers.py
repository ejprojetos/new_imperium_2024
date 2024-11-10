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
