from django.db import models
from commom.models import Address
import uuid
from django.utils import timezone
from users.models import User, Doctor, Patient


class Clinic(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    is_active = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    admin_clinic = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_clinic')

    def __str__(self):
        return self.name


class Appointment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"


class MedicalRecord(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_records')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='medical_records')
    allergies = models.TextField(blank=True)
    issues = models.TextField(blank=True)
    medication = models.TextField(blank=True)
    anamnesis = models.TextField(blank=True)
    new_medication = models.TextField(blank=True)
    exams = models.TextField(blank=True)

    def __str__(self):
        return f"Medical Record for {self.patient} by {self.doctor}"


class WorkingHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='working_hours')
    day_of_week = models.PositiveSmallIntegerField(
        choices=[(i, day) for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 1)]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.get_day_of_week_display()} from {self.start_time} to {self.end_time}"


class Notification(models.Model):
    MESSAGE_TYPES = [
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('alert', 'Alert'),
        ('reminder', 'Reminder'),
    ]
    
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=20, choices=MESSAGE_TYPES)
    datetime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return f"Notification for {self.user.email} - {self.get_type_display()}"