from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from aplicacion.models import *
# Create your views here.

def indexDefault(request):
    usuarios = Usuario.objects.all()
    cajasMenor = CajaMenor.objects.all()
    movimientos = Movimiento.objects.all()
    return render_to_response('index.html', {
    'Usuarios': usuarios, 'CajasMenor': cajasMenor});

def listaUsuarios(request):
    list = Usuario.objects.all()
    return render_to_response('usuarios/listaUsuarios.html', {'usuarios': list})

def listaCajaMenor(request):
    list = CajaMenor.objects.all()
    return render_to_response('cajaMenor/listaCajaMenor.html', {'cajaMenor': list})
