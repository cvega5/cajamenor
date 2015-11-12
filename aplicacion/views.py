from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from aplicacion.models import *
from aplicacion.forms import *
# Create your views here.

def indexDefault(request):
    usuarios = Usuario.objects.all()
    cajasMenores = CajaMenor.objects.all()
    movimientos = Movimiento.objects.all()
    return render_to_response('index.html', {
    'usuarios': usuarios, 'cajasMenor': cajasMenores});

def agregar(request, form, respuesta, modelo):
    if request.method=="POST":
        formulario = form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/"+respuesta)
    else:
        formulario = form()
    return render_to_response('formulario.html', {'formulario': formulario,
        'modelo': modelo, 'respuesta': respuesta}, context_instance=RequestContext(request))

def listaUsuarios(request):
    list = Usuario.objects.all()
    return render_to_response('usuarios/listaUsuarios.html', {'usuarios': list})

def listaCajaMenor(request):
    list = CajaMenor.objects.all()
    return render_to_response('cajaMenor/listaCajaMenor.html', {'cajaMenor': list})


def agregarUsuario(request):
	return agregar(request, UsuarioForm, respuesta = "usuarios", modelo = "Usuario")
