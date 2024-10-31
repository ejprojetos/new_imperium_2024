from rest_framework import viewsets, status, permissions
from rest_framework.response import Response 
from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from users.permissions import IsRoleUser

# Create your views here.
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    required_roles = ['Doctor']
    permission_classes = [IsRoleUser]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']