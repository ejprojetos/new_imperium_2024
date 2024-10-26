from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class ClinicAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer

#     def create(self, request, *args, **kwargs):
#         user = request.data.get('user')
        
#         role, created = Role.objects.get_or_create(name='Doctor')
        
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         doctor = serializer.save()

#         UserRole.objects.get_or_create(user=doctor.user, role=role)
        
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Patient, Role, UserRole
# from .serializers import PatientSerializer

# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

#     def create(self, request, *args, **kwargs):
#         user = request.data.get('user')

#         role, created = Role.objects.get_or_create(name='Patient')

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         patient = serializer.save()

#         UserRole.objects.get_or_create(user=patient.user, role=role)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import Receptionist, Role, UserRole
# from .serializers import ReceptionistSerializer

# class ReceptionistViewSet(viewsets.ModelViewSet):
#     queryset = Receptionist.objects.all()
#     serializer_class = ReceptionistSerializer

#     def create(self, request, *args, **kwargs):
#         user = request.data.get('user')

#         role, created = Role.objects.get_or_create(name='Receptionist')

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         receptionist = serializer.save()

#         UserRole.objects.get_or_create(user=receptionist.user, role=role)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# from rest_framework import viewsets
# from .models import ClinicAdmin
# from .serializers import ClinicAdminSerializer

# class ClinicAdminViewSet(viewsets.ModelViewSet):
#     queryset = ClinicAdmin.objects.all()
#     serializer_class = ClinicAdminSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def list(self, request, *args, **kwargs):
#         return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     def retrieve(self, request, *args, **kwargs):
#         return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     def update(self, request, *args, **kwargs):
#         return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     def partial_update(self, request, *args, **kwargs):
#         return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     def destroy(self, request, *args, **kwargs):
#         return Response({"detail": "Método não permitido."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
