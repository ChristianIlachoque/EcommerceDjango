from django import forms

from .models import VentaDetalles

class VentaDetallesForm(forms.ModelForm):
    class Meta:
        model = VentaDetalles
        fields = [
            'idVenta',
            'idProducto',
            'cantidad',
            'precio',
        ]