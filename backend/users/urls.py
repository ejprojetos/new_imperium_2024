from django.urls import path
from .views import AdminClinicRegisterView, DoctorRegisterView, PacientRegisterView, RecepcionistRegisterView

urlpatterns = [
    path('register/admin-clinic/', AdminClinicRegisterView.as_view(), name='register_admin_clinic'),
    path('register/doctor/', DoctorRegisterView.as_view(), name='register_doctor'),
    path('register/pacient/', PacientRegisterView.as_view(), name='register_pacient'),
    path('register/recepcionist/', RecepcionistRegisterView.as_view(), name='register_recepcionist'),
]
