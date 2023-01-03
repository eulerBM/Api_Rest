from django.db import models

class car_list(models.Model):
    marca = models.CharField(max_length=30)
    nome = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=20)

# Create your models here.
