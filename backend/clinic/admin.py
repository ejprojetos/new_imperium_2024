from django.contrib import admin
from .models import Clinic, Appointment, MedicalRecord, WorkingHours, Room, WaitingList


class ClinicAdmin(admin.ModelAdmin):
    list_display = ['name', 'cnpj', 'is_active']
    search_fields = ['name', 'cnpj']
    list_filter = ['is_active']
    list_editable = ['is_active']
    ordering = ['name']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'clinic', 'appointment_date', 'status']
    search_fields = ['patient__user__first_name', 'patient__user__last_name', 'doctor__user__first_name', 'doctor__user__last_name']
    list_filter = ['status']
    ordering = ['appointment_date']


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'allergies', 'issues', 'medication']
    search_fields = ['appointment__patient__user__first_name', 'appointment__patient__user__last_name', 'appointment__doctor__user__first_name', 'appointment__doctor__user__last_name']
    ordering = ['appointment']


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ['user', 'day_of_week', 'start_time', 'end_time']
    search_fields = ['user__first_name', 'user__last_name']
    list_filter = ['day_of_week']
    ordering = ['user', 'day_of_week']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['clinic', 'number', 'description']
    search_fields = ['clinic__name']
    list_filter = ['clinic']
    ordering = ['clinic', 'number']


class WaitingListAdmin(admin.ModelAdmin):
    list_display = ['patient', 'clinic', 'arrival_datetime', 'status', 'doctor']
    search_fields = ['patient__user__first_name', 'patient__user__last_name', 'doctor__user__first_name', 'doctor__user__last_name']
    list_filter = ['status']
    ordering = ['arrival_datetime']
    search_fields = ['user', 'day_of_week', 'start_time', 'end_time']
    list_per_page = 10


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(WorkingHours, WorkingHoursAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(WaitingList, WaitingListAdmin)
