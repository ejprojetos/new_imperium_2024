from rest_framework import serializers
from .models import MedicalRecord, Appointment, Room, Notification
from users.models import Patient, Doctor

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
