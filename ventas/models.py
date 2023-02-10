from django.db import models

# Create your models here.

class Venta(models.Model):
    idUsuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=3)