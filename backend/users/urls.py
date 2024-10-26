<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClinicAdminViewSet
from patient.views import MedicalFileViewSet

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     PatientViewSet,
#     DoctorViewSet,
#     ReceptionistViewSet,
#     ClinicAdminViewSet
# )

router = DefaultRouter()
router.register(r'patients', ClinicAdminViewSet)
router.register(r'medicalfile',MedicalFileViewSet)
# router.register(r'doctors', DoctorViewSet)
# router.register(r'receptionists', ReceptionistViewSet)
# router.register(r'clinic-admins', ClinicAdminViewSet)


urlpatterns = [
    # path('users/admin-clinic', ClinicAdminViewSet.as_view(), name='create-admin-clinic'),
    path('', include(router.urls)),  # Use the router's URLs
]

# urlpatterns = [
#     path('users/', UserView.as_view()),
#     path('patients', PatientViewSet.as_view()),
#     path('doctors', DoctorViewSet.as_view()),
#     path('', include(router.urls)),  # Use the router's URLs
# ]
=======
from django.urls import path
from .views import AdminClinicRegisterView, DoctorRegisterView, PacientRegisterView, RecepcionistRegisterView

urlpatterns = [
    path('register/admin-clinic/', AdminClinicRegisterView.as_view(), name='register_admin_clinic'),
    path('register/doctor/', DoctorRegisterView.as_view(), name='register_doctor'),
    path('register/pacient/', PacientRegisterView.as_view(), name='register_pacient'),
    path('register/recepcionist/', RecepcionistRegisterView.as_view(), name='register_recepcionist'),
]
>>>>>>> main
