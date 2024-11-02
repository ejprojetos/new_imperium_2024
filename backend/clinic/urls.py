from django.urls import path, include
from .views import RoomViewSet


urlpatterns = [
    path('<int:clinic_id>/rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:clinic_id>/rooms/<uuid:uuid>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]