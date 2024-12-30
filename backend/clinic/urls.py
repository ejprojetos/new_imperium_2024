from django.urls import path, include
from .views import RoomViewSet, MedicalRecordViewSet, NotificationViewSet, ClinicViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Endpoint para lista e criação
    path('', ClinicViewSet.as_view({'get': 'list', 'post': 'create'}), name='clinic-list'),
    # Endpoint para ações em objetos específicos
    path('<int:clinic_id>/', ClinicViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='clinic-detail'),
    path('medical-records/', MedicalRecordViewSet.as_view({'post': 'create'})),
    path('medical-records/appointment/<int:appointment_id>/', MedicalRecordViewSet.as_view({'get': 'list'})),
    path('medical-records/<int:pk>/', MedicalRecordViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('notifications/user/<int:user_id>/', NotificationViewSet.as_view({'get': 'list'})),
    path('notifications/<int:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:clinic_id>/rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:clinic_id>/rooms/<uuid:uuid>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]