from rest_framework import viewsets, status, permissions, filters

from rest_framework.response import Response 
from .models import MedicalRecord, Appointment, Room, Clinic, Notification
from .serializers import MedicalRecordSerializer, RoomSerializer, NotificationSerializer
from users.permissions import IsRoleUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .pagination import SmallPagination
from django_filters.rest_framework import DjangoFilterBackend

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

class NotificationViewSet(viewsets.ModelViewSet):
    """
        The `NotificationViewSet` allows users to view, update and delete their notifications. 
        Users can retrieve a list of notifications, filter them by type, read status, and date, 
        and manage the status of each notification (marking them as read or unread).
    """

    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get','put','delete']
    pagination_class = SmallPagination # difinindo uma paginação de 5 elementos por pagina
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['type','datetime', 'is_read']   
    ordering_fields = ('datetime',)
    lookup_field = 'pk'

    def get_queryset(self):
        # para as rotas que nescessitam do user_id
        user_id = self.kwargs.get('user_id')
        if user_id is not None:
            return Notification.objects.filter(user_id=user_id)

    def retrieve(self, request, *args, **kwargs):
        notification_pk = self.kwargs.get('pk')
        if notification_pk is not None:
            notification = Notification.objects.filter(pk=notification_pk).first()
            if notification:
                serializer = self.get_serializer(notification)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        notification_pk = self.kwargs.get('pk')
        notification = Notification.objects.filter(pk=notification_pk).first()
        if not notification:
            return Response({'detail': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(notification, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def destroy(self, request, *args, **kwargs):
        notification_id = self.kwargs['pk']
        notification = Notification.objects.get(id=notification_id)
        self.perform_destroy(notification)

        return Response({'detail': 'notification deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)