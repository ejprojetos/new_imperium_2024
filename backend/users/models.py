from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from commom.models import Address
from enum import Enum

def get_upload_path(instance, filename):
    return f"users/{instance.first_name}/{filename}"

class Expedient(models.Model):
    days_of_week = models.JSONField(default=list)
    turns = models.JSONField(default=list)

class RoleEnum(Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    PATIENT = "patient"
    RECEPTIONIST = "receptionist"

    @classmethod
    def choices(cls):
        return [(role.name, role.value) for role in cls]


class Role(models.Model):
    name = models.CharField(max_length=255, choices=RoleEnum.choices())
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
    first_name = models.CharField(max_length=255, blank=True)
    # last_name = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    cpf = models.CharField(max_length=255)
    date_birth = models.DateField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    clinics = models.ManyToManyField("clinic.Clinic", blank=True)
    #clinic = models.ForeignKey("clinic.Clinic", on_delete=models.CASCADE, blank=True, null=True)
    specialty = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    formacao = models.CharField(max_length=255, null=True, blank=True)
    crm = models.CharField(max_length=255, null=True, blank=True)
    attach_document = models.FileField(upload_to='attach',null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    expedient = models.OneToOneField(Expedient, on_delete=models.CASCADE, blank=True, null=True)
    availableForShift = models.BooleanField(default=False, blank=True, null=True)

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
        return self.role.name == role_name if self.role else False


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

class UserPolicies(models.Model):
    profile = models.CharField(max_length=255, choices=RoleEnum.choices())
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return super().__str__()
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

class UserSupport(models.Model):
    title = models.CharField(max_length=255)
    profile = models.CharField(max_length=255, choices=RoleEnum.choices())
    manual_archive = models.FileField(upload_to='manual',null=True, blank=True)

class FAQ(models.Model):
    title = models.CharField(max_length=255)
    questions = models.CharField(max_length=255)
    profile = models.CharField(max_length=255, choices=RoleEnum.choices())
    date = models.DateField(default=timezone.now)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

