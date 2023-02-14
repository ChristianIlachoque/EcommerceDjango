from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(max_length=100, default='sin_correo@gmail.com')
    clave = models.CharField(max_length=50, default='sin_clave')
