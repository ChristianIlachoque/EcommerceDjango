from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    edad = models.TextField()