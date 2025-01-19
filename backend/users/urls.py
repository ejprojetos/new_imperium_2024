from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import AdminViewSet, DoctorViewSet, PatientViewSet, ReceptionistViewSet, 
from .views import CustomTokenObtainPairView, ViewGetUsersDoctors, ViewGetUsersRecepcionistas, ViewGetUsersPacientes, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from clinic.views import MedicalRecordViewSet, WaitingListViewSet, WorkingHoursViewSet, AppointmentViewSet

# router = DefaultRouter()
# router.register(r'admins', AdminViewSet, basename='users/admin')
# router.register(r'doctors', DoctorViewSet, basename='users/doctor')
# router.register(r'patients', PatientViewSet, basename='users/patient')
# router.register(r'receptionists', ReceptionistViewSet, basename='users/receptionist')

from .views import UserViewSet
router = DefaultRouter()
router.register('users', UserViewSet, basename='users/')

router.register(r'waiting-list', WaitingListViewSet, basename='waiting-list')
# router.register(r'working-hours', WorkingHoursViewSet, basename='working-hours')
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('users/users_doctors', ViewGetUsersDoctors.as_view(), name='list_users_clinic'),
    path('users/users_recepcionistas', ViewGetUsersRecepcionistas.as_view(), name='list_users_recepcionistas'),
    path('users/users_pacientes', ViewGetUsersPacientes.as_view(), name='list_users_pacientes') 

    # path('users/', UserViewSet.as_view(), name='users')
]