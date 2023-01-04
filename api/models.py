from django.db import models

class lista_de_carros(models.Model):
    id_carro = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=30)
    nome = models.CharField(max_length=50)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

# Create your models here.
