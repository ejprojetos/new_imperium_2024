from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from clinic.models import Clinic
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Role(models.Model):
    """Model repres enting a user role."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """Manager for User model."""
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Designates whether the user can log into the admin site
    date_joined = models.DateTimeField(auto_now_add=True)
    roles = models.ManyToManyField(Role, related_name='users', blank=True)  # Many-to-many relationship with Role

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']  # Required fields for creating a user

    def __str__(self):
        return self.username