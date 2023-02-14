from django.db import models

# Create your models here.

class VentaDetalles(models.Model):
    idVenta = models.ForeignKey('ventas.Venta', on_delete=models.CASCADE)
    idProducto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=3)
