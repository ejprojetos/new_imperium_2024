from django.contrib import admin
from .models import Clinic, Appointment, MedicalRecord, WorkingHours, Room

class ClinicAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnpj', 'is_active', 'address', 'admin_clinic']
    search_fields = ['name', 'cnpj']
    list_filter = ['is_active']
    list_per_page = 10


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'clinic', 'appointment_date', 'reason', 'status']
    search_fields = ['patient', 'doctor', 'clinic', 'appointment_date', 'reason']
    list_filter = ['status']
    list_per_page = 10


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'allergies', 'issues', 'medication', 'anamnesis', 'new_medication', 'exams']
    search_fields = ['appointment', 'allergies', 'issues', 'medication', 'anamnesis', 'new_medication', 'exams']
    list_per_page = 10


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ['user', 'day_of_week', 'start_time', 'end_time']
    search_fields = ['user', 'day_of_week', 'start_time', 'end_time']
    list_per_page = 10


class RoomAdmin(admin.ModelAdmin):
    list_display = ['clinic', 'number']
    search_fields = ['clinic', 'number', 'description']
    list_per_page = 10


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(WorkingHours, WorkingHoursAdmin)
admin.site.register(Room, RoomAdmin)
