from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AdminClinicSerializer, DoctorRegisterSerializer, PacientRegisterSerializer, RecepcionistRegisterSerializer
from .permissions import RolePermission
from .models import Role


class AdminClinicRegisterView(APIView):
    permission_classes = [AllowAny]  # No authentication required

    @extend_schema(
        summary="Registrar um Admin da Clínica",
        description="Endpoint para registrar um usuário com o papel de admin-clinic.",
        request=AdminClinicSerializer,
        responses={201: AdminClinicSerializer, 400: "Erro de validação nos dados"}
    )
    def post(self, request):
        serializer = AdminClinicSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user without roles in the request
            # Automatically assign the 'admin-clinic' role
            admin_role, _ = Role.objects.get_or_create(name='admin-clinic')
            user.roles.add(admin_role)  # Add the role to the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorRegisterView(APIView):
    permission_classes = [RolePermission]  # Requires authentication and specific role

    @extend_schema(
        summary="Registrar um Médico",
        description="Endpoint para registrar um usuário com o papel de doctor.",
        request=DoctorRegisterSerializer,
        responses={201: DoctorRegisterSerializer, 400: "Erro de validação nos dados"}
    )
    def post(self, request):
        serializer = DoctorRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user without roles in the request
            # Automatically assign the 'doctor' role
            doctor_role, _ = Role.objects.get_or_create(name='doctor')
            user.roles.add(doctor_role)  # Add the role to the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PacientRegisterView(APIView):
    permission_classes = [RolePermission]  # Requires authentication and specific role

<<<<<<< HEAD
"""
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user')

        role, created = Role.objects.get_or_create(name='Patient')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()

        UserRole.objects.get_or_create(user=patient.user, role=role)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""

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
=======
    @extend_schema(
        summary="Registrar um Paciente",
        description="Endpoint para registrar um usuário com o papel de pacient.",
        request=PacientRegisterSerializer,
        responses={201: PacientRegisterSerializer, 400: "Erro de validação nos dados"}
    )
    def post(self, request):
        serializer = PacientRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user without roles in the request
            # Automatically assign the 'pacient' role
            pacient_role, _ = Role.objects.get_or_create(name='pacient')
            user.roles.add(pacient_role)  # Add the role to the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecepcionistRegisterView(APIView):
    permission_classes = [RolePermission]  # Requires authentication and specific role

    @extend_schema(
        summary="Registrar um Recepcionista",
        description="Endpoint para registrar um usuário com o papel de recepcionist.",
        request=RecepcionistRegisterSerializer,
        responses={201: RecepcionistRegisterSerializer, 400: "Erro de validação nos dados"}
    )
    def post(self, request):
        serializer = RecepcionistRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user without roles in the request
            # Automatically assign the 'recepcionist' role
            recepcionist_role, _ = Role.objects.get_or_create(name='recepcionist')
            user.roles.add(recepcionista_role)  # Add the role to the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> main
