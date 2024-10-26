from django.db import models
from commom.models import Address

class Clinic(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=255, null=True, blank=True)