from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.TextField(max_length=100)
    edad = models.IntegerField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="productos")
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    stock = models.IntegerField()
    descuento = models.BooleanField(blank=True)

class Venta(models.Model):
    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=3)

class Detalle_Venta(models.Model):
    idVenta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    idProducto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)
