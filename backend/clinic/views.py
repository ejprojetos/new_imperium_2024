from rest_framework import viewsets, status, permissions
from rest_framework.response import Response 
from .models import MedicalRecord, Appointment, Room, Clinic, WaitingList, Doctor, WorkingHours
from .serializers import MedicalRecordSerializer, RoomSerializer, WaitingListSerializer, AssignDoctorSerializer
from users.permissions import IsRoleUser
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


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

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    lookup_field = 'uuid'  # Define o campo de busca como 'uuid'

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        clinic_id = self.kwargs['clinic_id']
        return Room.objects.filter(clinic_id=clinic_id)

    def create(self, request, *args, **kwargs):
        clinic_id = self.kwargs['clinic_id']
        clinic = get_object_or_404(Clinic, id=clinic_id)
        
        serializer = self.get_serializer(data=request.data, context={'clinic': clinic})
        if serializer.is_valid():
            serializer.save(clinic=clinic)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        clinic_id = self.kwargs['clinic_id']
        clinic = get_object_or_404(Clinic, id=clinic_id)

        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'clinic': clinic})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class WaitingListViewSet(viewsets.ModelViewSet):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer
    required_roles = ['Recepcionist', 'Doctor']
    permission_classes = [IsRoleUser]
    http_method_names = ['post', 'delete', 'put']
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def get_serializer_class(self):
        # Usar AssignDoctorSerializer apenas para a ação assign_doctor
        if self.action == 'assign_doctor':
            return AssignDoctorSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        waiting_list_item = self.get_object()
        waiting_list_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['put'], url_path='assign-doctor')
    def assign_doctor(self, request, pk=None):
        waiting_list = self.get_object()  # Obtém a instância da lista de espera
        serializer = AssignDoctorSerializer(data=request.data, context={'waiting_list': waiting_list})

        if serializer.is_valid():
            doctor_id = serializer.validated_data['doctor_id']
            waiting_list.doctor_id = doctor_id
            waiting_list.status = "in_progress"
            waiting_list.save()
            return Response({"detail": "Doctor assigned successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
