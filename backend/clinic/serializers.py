from rest_framework import serializers
from .models import MedicalRecord, Appointment
from users.models import Patient, Doctor

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.ReadOnlyField(source='appointment.patient.id')
    doctor = serializers.ReadOnlyField(source='appointment.doctor.id')
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = MedicalRecord
        fields = ['uuid', 'patient', 'doctor', 'appointment', 'allergies', 'issues', 'medication', 'anamnesis', 'new_medication', 'exams']
        read_only_fields = ['uuid']
