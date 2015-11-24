from django import forms
from django.forms import *
from aplicacion.models import *
from django.contrib.auth.models import User

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

class MovimientoForm(ModelForm):
	class Meta:
		model = Movimiento
		exclude = ('eliminado', 'idRubro')
		widgets = {
        'fecha': DateInput(attrs={'placeholder': 'Ingrese la Fecha ( dd/mm/aa )', 'class': "form-control"}),
		'cajamenor': Select(attrs={'class': "form-control"}),
		'valorEnLetras': TextInput(attrs={'placeholder': 'Dinero total asignado (en letras)', 'class': "form-control"}),
		'valorTransaccion': TextInput(attrs={'placeholder': 'Dinero total asignado (en cantidad)', 'class': "form-control"}),
        'descripcion': Textarea(attrs={'placeholder': 'Uso del dinero', 'class': "form-control"})}

class ParametroForm(ModelForm):
	class Meta:
		model = Parametro
		fields = '__all__'
		widgets = {
		'atributo': TextInput(attrs={'placeholder': 'Atributo', 'class': "form-control"}),
		'descripcion': Textarea(attrs={'placeholder': 'Descripcion', 'class': "form-control"}),
		'estadoParametro': NumberInput(attrs={'placeholder': 'Estado',  'class': "form-control"}),}

class ValorParametroForm(ModelForm):
	class Meta:
		model = ValorParametro
		exclude = ('parametro', )
		widgets = {
		'valor': TextInput(attrs={'placeholder': 'Valor'}),
		'orden': NumberInput(attrs={'placeholder': 'Estado'}),
		'estado': NumberInput(attrs={'placeholder': 'Estado'}),}

class eliminarUsuarioForm(ModelForm):
	class Meta:
		model = Usuario
		fields = ('eliminado',)

class eliminarCajaMenorForm(ModelForm):
	class Meta:
		model = CajaMenor
		fields = ('eliminado',)
