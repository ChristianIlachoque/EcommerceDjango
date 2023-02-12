from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):
    clave = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'edad',
            'correo',
            'clave',
        ]