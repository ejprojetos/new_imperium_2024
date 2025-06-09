from .models import User
from .serializers import UserSerializer, RecepcionistSerializer, UserPoliciesSerializer, FAQSerializer, UserSupportSerializer
from rest_framework import permissions
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

from rest_framework import permissions, viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

from .models import User, Role, Expedient, UserPolicies, FAQ, UserSupport
from .serializers import UserSerializer, CustomTokenObtainPairSerializer, ExpedientSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from clinic.pagination import FaqPagination, SmallPagination
from clinic.models import WorkingHours
from .permissions import IsRoleUser

from datetime import time

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['email', 'first_name', 'cpf', 'date_birth', 'clinics__name', 'specialty', 'gender', 'formacao', 'phone']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    lookup_field = 'pk'
    
    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['retrieve', 'create']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user

        # filtrar por dias da semana e turnos
        days_of_week = self.request.query_params.getlist('days_of_week', [])
        turns = self.request.query_params.getlist('turns', [])

        if days_of_week and turns:
            return self.queryset.filter(expedient__days_of_week__contains=days_of_week, expedient__turns__contains=turns)
        elif turns:
            return self.queryset.filter(expedient__turns__contains=turns)
        elif days_of_week:
            return self.queryset.filter(expedient__days_of_week__contains=days_of_week)
        
        if user.is_staff:  # Admin pode visualizar usuários de todas as clínicas
            return User.objects.all()
        
        return User.objects.all()  # Usuários podem ver somente da clínica associada

    def list_users_from_clinic(self, request):
        user = request.user
        if user.is_staff or user.has_role('RECEPTIONIST'):  # Verifica se o usuário é admin ou receptionist
            clinic_users = self.get_queryset()
            serializer = self.get_serializer(clinic_users, many=True)
            return Response(serializer.data)
        return Response({"detail": "Você não tem permissão para visualizar os usuários."}, status=403)

    def perform_destroy(self, instance):
        user = self.request.user
        if user.is_staff or user.has_role('RECEPTIONIST'):  # Admin e receptionist podem deletar
            if user.is_staff or instance in user.clinics.all():  # receptionist só pode excluir da própria clínica
                instance.delete()
            else:
                raise PermissionDenied("Você não tem permissão para excluir esse usuário.")
        else:
            raise PermissionDenied("Somente admins ou receptionists podem excluir usuários.")
    
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Validação adicional ou criação de roles pode ser feita aqui, se necessário
            user = serializer.save()
            return Response({"detail": "Usuário criado com sucesso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        user = self.request.user
        role = serializer.validated_data.get('role')
        if role is None:
            role = Role.objects.get(name='PATIENT')
            role = {
                "name": role.name
            }

        # liberar a criação de usuários apenas para PATIENTS para usuários não autenticados
        if self.request.user.is_authenticated:
            if user.is_staff:
                serializer.save()
            elif role in ('DOCTOR', 'RECEPTIONIST', 'PATIENT'):
                if user.has_role('RECEPTIONIST') or user.has_role('ADMIN'):
                    serializer.save()
                else:
                    raise PermissionDenied("Você não tem permissão para criar esse tipo de usuário.")
            else:
                raise PermissionDenied("Somente administradores ou recepcionistas podem criar doctores, receptionists e patients.")
        elif role["name"] in "PATIENT":
            serializer.save()
        else:
            raise PermissionDenied("Você não tem permissão para criar esse tipo de usuário.")
        
    def update(self, request, *args, **kwargs):
        # permintindo que o admin atualize qualquer usuário e o usuário atualize apenas seus próprios dados
        user = request.user
        if user.is_staff:  # Admin pode atualizar qualquer usuário
            return super().update(request, *args, **kwargs)
        elif user.id == int(kwargs['pk']):  # Usuário pode editar apenas seus próprios dados
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied("Você não tem permissão para editar este usuário.")

    @action(detail=True, methods=['patch'])
    def update_role(self, request, pk=None):
        user = self.get_object()
        current_user = request.user
        if current_user.is_staff:  # Apenas admins podem alterar os papéis
            role_data = request.data.get('role')
            if role_data:
                role = Role.objects.get(name=role_data['name'])
                user.role = role
                user.save()
                return Response({"detail": "Papéis atualizados com sucesso."})
            else:
                return Response({"detail": "Nenhum papel fornecido."}, status=400)
        else:
            raise PermissionDenied("Somente administradores podem alterar papéis.")

from django.http import JsonResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import serializers
from .models import User

# View para buscar apenas os médicos
@extend_schema(
    summary="List Doctors",
    description="Returns a list of users with the 'DOCTOR' role.",
    responses={
        200: UserSerializer(many=True),
        401: "Authentication credentials were not provided.",
    }
)
class ViewGetUsersDoctors(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(role__name='DOCTOR')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    summary="List Receptionists",
    description="Returns a list of users with the 'RECEPTIONIST' role.",
    responses={
        200: RecepcionistSerializer(many=True),
        401: "Authentication credentials were not provided.",
    }
)
class ViewGetUsersRecepcionistas(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(role__name='RECEPTIONIST')
        serializer = RecepcionistSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@extend_schema(
    summary="List Pacients",
    description="Returns a list of users with the 'PATIENT' role.",
    responses={
        200: UserSerializer(many=True),
        401: "Authentication credentials were not provided.",
    }
)
class ViewGetUsersPacientes(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(role__name='PATIENT')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomRefreshObtainPairSerializer
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomRefreshObtainPairSerializer


    
@extend_schema(
    summary="List Clinics",
    description="Returns a list of clinics.",
    responses={
        200: UserSerializer(many=True),
        401: "Authentication credentials were not provided.",
    }
)
class ViewGetUsersPacientes(APIView):
    def get(self, request, *args, **kwargs):
        user = self.request.user

        users = User.objects.filter(role__name__in=['PATIENT'])
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from clinic.serializers import ClinicSerializer

@extend_schema(
    summary="List Clinics by User",
    description="Returns all clinics associated with the authenticated user.",
    responses={
        200: ClinicSerializer(many=True),
        401: "Authentication credentials were not provided.",
    },
)
class ViewGetUsersClinics(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user
        if not user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        clinics = user.clinics.all()  # Fetch clinics associated with the user
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserPoliciesViewSet(viewsets.ModelViewSet):
    queryset = UserPolicies.objects.all()
    serializer_class = UserPoliciesSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [permissions.IsAuthenticated]

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['title', 'profile']   
    pagination_class = FaqPagination

class UserSupportViewSet(viewsets.ModelViewSet):
    queryset = UserSupport.objects.all()
    serializer_class = UserSupportSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['profile']
    pagination_class = SmallPagination

class ExpedientViewSet(viewsets.ModelViewSet):
   days_dict = {
        "Segunda-feira": 1,
        "Terça-feira": 2,
        "Quarta-feira": 3,
        "Quinta-feira": 4,
        "Sexta-feira": 5,
        "Sábado": 6,
        "Domingo": 7
    }

   times = {
        "Matutino": [7, 12],
        "Vespertino": [13, 18],
        "Noturno": [18, 23],
    }   

   queryset = Expedient.objects.all()
   serializer_class = ExpedientSerializer
   required_roles = ['ADMIN']
   permission_classes = [IsRoleUser]
   http_method_names = ['get', 'put', 'delete']
      
   def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()

       serializer = self.get_serializer(instance, data=request.data, partial=partial)

       if serializer.is_valid():
           #atualizar o working hours
           user = serializer.validated_data.get('expedient_user')
           days = serializer.validated_data.get('days_of_week')
           turns = serializer.validated_data.get('turns')

           WorkingHours.objects.filter(user=user).delete()

           for day in days:
               for turn in turns:
                   #criar as working hours com base nos dias e turnos
                   working_hours = WorkingHours(user=user, day_of_week=self.days_dict[day], start_time=time(self.times[turn][0],0), end_time=time(self.times[turn][1],0))
                   working_hours.save()

           serializer.save()
           return Response(serializer.data)

       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
   def destroy(self, request, *args, **kwargs):
       user_id = self.kwargs.get('pk')
       user = User.objects.get(id=user_id)
       WorkingHours.objects.filter(user=user).delete()


       return super().destroy(request, *args, **kwargs)