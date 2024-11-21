from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, DoctorViewSet, PatientViewSet, ReceptionistViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clinic.views import MedicalRecordViewSet, WaitingListViewSet, WorkingHoursViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='users/admin')
router.register(r'doctors', DoctorViewSet, basename='users/doctor')
router.register(r'patients', PatientViewSet, basename='users/patient')
router.register(r'receptionists', ReceptionistViewSet, basename='users/receptionist')
router.register(r'medical-records', MedicalRecordViewSet, basename='medical-records')
router.register(r'waiting-list', WaitingListViewSet, basename='waiting-list')
router.register(r'working-hours', WorkingHoursViewSet, basename='working-hours')
router.register(r'appointments', AppointmentViewSet, basename='appointments')



urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]