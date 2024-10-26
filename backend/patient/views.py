from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import MedicalFile
from .serializers import MedicalFileSerializer

class MedicalFileViewSet(viewsets.ModelViewSet):
    queryset = MedicalFile.objects.all()
    serializer_class = MedicalFileSerializer