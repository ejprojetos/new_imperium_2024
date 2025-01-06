from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from commom.models import Address
from enum import Enum

class RoleEnum(Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"
    RECEPTIONIST = "receptionist"

    @classmethod
    def choices(cls):
        return [(role.name, role.value) for role in cls]


class Role(models.Model):
    name = models.CharField(max_length=20, choices=RoleEnum.choices())
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    cpf = models.CharField(max_length=11)
    date_birth = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    roles = models.ManyToManyField(Role, related_name='users')
    clinics = models.ManyToManyField("clinic.Clinic", blank=True)
    specialty = models.CharField(max_length=255, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_birth']

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
    
    def has_role(self, role_name):
        """Verifica se o usuário tem um determinado papel."""
        return self.roles.filter(name=role_name).exists()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    #date_of_birth = models.DateField()
    #medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return self.user.get_full_name()


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')

    def __str__(self):
        return self.user.get_full_name()


class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')

    def __str__(self):
        return self.user.get_full_name()

