from rest_framework import viewsets, status, permissions
from rest_framework.response import Response 
from .models import MedicalRecord, Appointment
from .serializers import MedicalRecordSerializer
from users.permissions import IsRoleUser

# Create your views here.
class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
        The `MedicalRecordViewSet` allows doctors and administrators to view, create medical records. 
        Only users with the role of doctor or administrator can access this view: doctors can create new records, 
        while both doctors and administrators can update existing records and view all records.
    """

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    required_roles = ['Doctor','Admin']
    permission_classes = [IsRoleUser]
    http_method_names = ['get', 'post', 'put']
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            appointment = serializer.validated_data.get('appointment')

            if MedicalRecord.objects.filter(appointment__id=appointment.id).exists():
                return Response({"detail": "it is not possible to create a medical record with the same appointment"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
