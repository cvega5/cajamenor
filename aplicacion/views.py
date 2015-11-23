from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from aplicacion.models import *
from aplicacion.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
# Create your views here.

def indexDefault(request):
	if request.user.is_authenticated():
		usuarios = Usuario.objects.all()
		cajasMenores = CajaMenor.objects.all()
		movimientos = Movimiento.objects.all()
		return render_to_response('index.html', {
			'usuarios': usuarios, 'cajasMenor': cajasMenores, 'movimientos': movimientos}, context_instance=RequestContext(request));
	else:
	   return redirect("/login")


def agregar(request, form, respuesta, modelo):
    if request.method=="POST":
        formulario = form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/"+respuesta)
    else:
        formulario = form()
    return render_to_response('aplicacion/formulario.html', {'formulario': formulario,
        'modelo': modelo, 'respuesta': respuesta}, context_instance=RequestContext(request))

def editar(request, form, id, Model, respuesta, modelo):
	item = Model.objects.get(id=id)
	if request.method=="POST":
		formulario = form(request.POST, instance=item)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form(instance=item)
	return render_to_response('aplicacion/ver-editar.html', { 'modelo': modelo, 'item': item.id,
		'formulario': formulario, 'valores': item, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
def listaUsuarios(request):
    list = Usuario.objects.all()
    return render_to_response('aplicacion/usuarios/listaUsuarios.html', {'usuarios': list})

@login_required(login_url='/login/')
def listaCajaMenor(request):
    list = CajaMenor.objects.all()
    return render_to_response('aplicacion/cajaMenor/listaCajaMenor.html', {'cajaMenor': list})

@login_required(login_url='/login/')
def listaMovimientos(request):
    list = Movimiento.objects.all()
    list2 = Parametro.objects.all()
    return render_to_response('aplicacion/movimiento/listaMovimientos.html', {'movimientos': list, 'parametros': list2})

@login_required(login_url='/login/')
def agregarUsuario(request):
	return agregar(request, UsuarioForm, respuesta = "usuarios", modelo = "usuario")

@login_required(login_url='/login/')
def editarUsuario(request, id):
	return editar(request, UsuarioForm, id, Usuario, respuesta = "usuarios", modelo = "usuario")

@login_required(login_url='/login/')
def agregarCajaMenor(request):
    return agregar(request, CajaMenorForm, respuesta = "cajaMenor", modelo = "Caja Menor")

@login_required(login_url='/login/')
def editarCajaMenor(request, id):
	return editar(request, CajaMenorForm, id, CajaMenor, respuesta = "cajaMenor", modelo = "caja menor")

@login_required(login_url='/login/')
def nuevoMovimiento(request):
    if request.POST:
        formulario = MovimientoForm(request.POST)
        if formulario.is_valid():
            item = formulario.save()
            caja= CajaMenor.objects.get(nombreCaja=item.cajamenor)
            caja.totalDisponible = caja.totalDisponible-item.valorTransaccion
            if(caja.totalDisponible>0):
                caja.save()
                item.save()
                return HttpResponseRedirect("/movimientos")
            else:
                return render_to_response('aplicacion/movimiento/formulario.html', {'formulario': formulario,
                    'modelo': Movimiento, 'caja': caja, 'respuesta': "movimiento"}, context_instance=RequestContext(request))
    else:
        formulario = MovimientoForm()
    return render_to_response('aplicacion/movimiento/formulario.html', {'formulario': formulario,
        'modelo': Movimiento, 'respuesta': "movimiento"}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editarMov(request, form, id, Model, respuesta, modelo):
    item = Model.objects.get(id=id)
    precioAnterior= item.valorTransaccion
    if request.POST:
        formulario = form(request.POST, instance=item)
        if formulario.is_valid():
            valorNuevo = formulario.save()
            caja= CajaMenor.objects.get(nombreCaja=valorNuevo.cajamenor)
            if item.cajamenor == caja.nombreCaja:
                caja.totalDisponible = (precioAnterior-valorNuevo.valorTransaccion)+ caja.totalDisponible
                caja.save()
                item.save()
                return HttpResponseRedirect("/movimientos")
            else:
                caja.totalDisponible = caja.totalDisponible - valorNuevo.valorTransaccion
                caja.save()
                item.save()
        else:
            return render_to_response('aplicacion/ver-editar.html', {'formulario': formulario,
                    'modelo': Movimiento, 'respuesta': "movimiento"}, context_instance=RequestContext(request))
    else:
        formulario = form(instance=item)
    return render_to_response('aplicacion/ver-editar.html', {'formulario': formulario,
        'modelo': Movimiento, 'respuesta': "movimiento", 'modelo': modelo }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editarmovimiento(request, id):
	return editarMov(request, MovimientoForm, id, Movimiento, respuesta = "movimientos", modelo = "Movimiento")
