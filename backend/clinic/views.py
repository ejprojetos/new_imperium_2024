from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Room, Clinic
from .serializers import RoomSerializer


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