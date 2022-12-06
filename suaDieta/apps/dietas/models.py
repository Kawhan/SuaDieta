from django.db import models
import datetime 
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


# Create your models here.
class Dieta(models.Model):
    dias_semana = (
        ("Seg", "Segunda-Feira"),
        ("Ter", "Terça-Feira"),
        ("Qua", "Quarta-Feira"),
        ("Qui", "Quinta-Feira"),
        ("Sex", "Sexta-feira"),
        ("Sab", "Sabado"),
        ("Dom", "Domingo"),
    )
    pessoa  = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_dieta = models.CharField(max_length=100)
    descricao = models.TextField()
    ingredientes = models.TextField()
    dias_semana = MultiSelectField(max_length=27, choices=dias_semana, blank=False, null=False, default="Seg" )
    carbo = models.IntegerField()
    calorias = models.IntegerField()
    dieta_concluida = models.BooleanField(default=False)
    data_inicio = models.DateField()
    data_final = models.DateField()


    def __str__(self):
        return self.ingredientes

    class Meta:
        verbose_name = "Dieta"