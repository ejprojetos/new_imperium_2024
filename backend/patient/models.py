from django.db import models
import uuid
from users.models import User

class Consult(models.Model):
    pass

# Create your models here.
class MedicalFile(models.Model):
    """
        model for modeling "prontuário"
    """
    class Meta:
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    patient = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Paciente',related_name='pacientes',null = True, blank=True)
    medic = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Médico',related_name='médicos',null = True, blank=True)
    appointment_date = models.DateTimeField(verbose_name = 'Data da consulta',null = True, blank=True)
    allergies = models.TextField(max_length = 400, verbose_name = 'Alergias')
    issues = models.TextField(max_length = 400,verbose_name = 'Problemas recorrentes')
    medication = models.TextField(max_length = 400,verbose_name = 'Medicação')
    anamnesis = models.TextField(max_length = 500,verbose_name = 'Anamnese')
    new_medication = models.TextField(max_length = 400,verbose_name = 'Nova medicação')
    exams = models.TextField(max_length = 400,verbose_name = 'Exames')
    consult = models.ForeignKey(Consult,on_delete=models.CASCADE,verbose_name='Consulta',related_name='consultas',null = True, blank=True)

    def __str__(self):
        return self.id