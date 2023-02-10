from django.contrib import admin

# Register your models here.
from .models import Usuario

admin.site.register(Usuario)
# admin.site.register(Producto)
# admin.site.register(Venta)
# admin.site.register(Detalle_Venta)