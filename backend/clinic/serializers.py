from rest_framework import serializers
from .models import MedicalRecord, Appointment
from users.models import Patient, Doctor

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = MedicalRecord
        fields = ['uuid', 'patient', 'doctor', 'appointment', 'allergies', 'issues', 'medication', 'anamnesis', 'new_medication', 'exams']
        read_only_fields = ['uuid']