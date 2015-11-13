from django import forms
from django.forms import *
from aplicacion.models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('eliminado',)
        widgets = {
        'identificacion': TextInput(attrs={'placeholder': 'Identificacion', 'class': "form-control", 'maxlenght': "15"}),
		'nombre': TextInput(attrs={'placeholder': 'Nombre', 'class': "form-control"}),
        'apellido': TextInput(attrs={'placeholder': 'Apellido', 'class': "form-control"}),
        'contrasena': TextInput(attrs={'placeholder': 'Password', 'type': 'Password', 'class': "form-control"})}

class CajaMenorForm(ModelForm):
    class Meta:
        model = CajaMenor
        exclude = ('eliminado',)
        widgets = {
        'nombreCaja': TextInput(attrs={'placeholder': 'Nombre de la Caja menor', 'class': "form-control"}),
		'usuario': Select(attrs={'class': "form-control"}),
        'totalDisponible': TextInput(attrs={'placeholder': 'Dinero total asignado', 'class': "form-control"})}
