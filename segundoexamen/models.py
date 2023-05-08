from django.db import models


# Create your models here.

class clientes(models.Model):
    celular = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=70, blank=True, unique=True)

class habitaciones(models.Model):
    tipo = models.CharField(max_length=100)
    precio = models.IntegerField(blank=True, null=True)

class reservas(models.Model):
    noches = models.IntegerField(blank=True, null=True)
    huespedes = models.IntegerField(blank=True, null=True)
