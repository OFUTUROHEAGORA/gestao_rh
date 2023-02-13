from django.db import models
from Funcionarios.models import Funcionario

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.motivo