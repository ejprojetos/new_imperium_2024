from django.urls import path, include
from .views import RoomViewSet, MedicalRecordViewSet, NotificationViewSet#, ClinicViewSet, AppointmentViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('notifications/user/<int:user_id>', NotificationViewSet.as_view({'get': 'list'})),
    path('notifications/<int:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:clinic_id>/rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:clinic_id>/rooms/<uuid:uuid>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]