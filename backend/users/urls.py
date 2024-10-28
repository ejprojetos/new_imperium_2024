from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, DoctorViewSet, PatientViewSet, ReceptionistViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='users/admin')
router.register(r'doctors', DoctorViewSet, basename='users/doctor')
router.register(r'patients', PatientViewSet, basename='users/patient')
router.register(r'receptionists', ReceptionistViewSet, basename='users/receptionist')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]