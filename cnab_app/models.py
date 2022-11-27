from django.db import models


class Cnab(models.Model):
    type = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    cpf = models.CharField(max_length=20)
    cartao = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    dono = models.CharField(max_length=20)
    loja = models.CharField(max_length=20)
