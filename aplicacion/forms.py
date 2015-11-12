from django import forms
from django.forms import *
from aplicacion.models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ('eliminado',)
        widgets = {
        'identificacion': TextInput(attrs={'placeholder': 'Identificacion', 'class': "inputText"}),
		'nombre': TextInput(attrs={'placeholder': 'Nombre', 'class': "inputText"}),
        'apellido': TextInput(attrs={'placeholder': 'Apellido', 'class': "inputText"}),
        'contrasena': TextInput(attrs={'placeholder': 'Password', 'type': 'Password', 'class': "inputText"})}

class CajaMenorForm(ModelForm):
    class Meta:
        model = CajaMenor
        exclude = ('eliminado',)
        widgets = {
        'nombreCaja': TextInput(attrs={'placeholder': 'Nombre de la nueva Caja menor', 'class': "inputText"}),
		'Usuario': Select(attrs={'placeholder': 'Asignar Usuario', 'class': "ui dropdown"}),
        'Cantidad Inicial': NumberInput(attrs={'placeholder': 'Cantidad administrada por la caja', 'class': "inputText"})}
