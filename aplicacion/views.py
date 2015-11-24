from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from aplicacion.models import *
from aplicacion.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
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
	return render_to_response('aplicacion/ver-editar.html', { 'modelo': modelo, 'item': item,
		'formulario': formulario, 'valores': item, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
def listaUsuarios(request):
    list = Usuario.objects.filter(eliminado=False)
    return render_to_response('aplicacion/usuarios/listaUsuarios.html', {'usuarios': list}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def listaCajaMenor(request):
	if request.user.is_staff:
		list = CajaMenor.objects.filter(eliminado=False)
		return render_to_response('aplicacion/cajaMenor/listaCajaMenor.html', {'cajaMenor': list}, context_instance=RequestContext(request))
	else:
		current_user = request.user
		list = sorted(CajaMenor.objects.filter(eliminado=False), key=lambda current_user: current_user.usuario)
		return render_to_response('aplicacion/cajaMenor/listaCajaMenor.html', {'cajaMenor': list}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def listaMovimientos(request):
    list = Movimiento.objects.filter(eliminado=False)
    return render_to_response('aplicacion/movimiento/listaMovimientos.html', {'movimientos': list}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarUsuario(request):
	return agregarUser(request, UsuarioForm, respuesta = "usuarios", modelo = "usuario")


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def editarUsuario(request, id):
	return editar(request, UsuarioForm, id, Usuario, respuesta = "Usuario", modelo = "usuario")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarCajaMenor(request):
    return agregar(request, CajaMenorForm, respuesta = "cajaMenor", modelo = "Caja Menor")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
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
            caja.save()
            item.save()
            return HttpResponseRedirect("/movimientos")
    else:
        formulario = MovimientoForm()
    return render_to_response('aplicacion/movimiento/formulario.html', {'formulario': formulario,
        'modelo': Movimiento, 'respuesta': "movimiento", 'modelo': "movimiento"}, context_instance=RequestContext(request))

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
            return render_to_response('aplicacion/ver-editar.html', {'formulario': formulario, 'item': item,
                    'modelo': Movimiento, 'respuesta': "movimiento"}, context_instance=RequestContext(request))
    else:
        formulario = form(instance=item)
    return render_to_response('aplicacion/ver-editar.html', {'formulario': formulario, 'item': item,
        'modelo': Movimiento, 'respuesta': "movimiento", 'modelo': modelo }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def editarmovimiento(request, id):
	return editarMov(request, MovimientoForm, id, Movimiento, respuesta = "movimientos", modelo = "Movimiento")


@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarUsuario(request):
	return agregarUser(request, UsuarioForm, respuesta = "usuarios", modelo = "usuario")

def agregarUser(request, form, respuesta, modelo):
    if request.method=="POST":
        formulario = form(request.POST, request.FILES)
        if formulario.is_valid():
            newUser = formulario.save()
            if User.objects.filter(username=newUser.identificacion):
                raise forms.ValidationError('Nombre de usuario ya registrado.')
            else:
            	user = User.objects.create_user(username=newUser.identificacion, email=newUser.nombre, password=newUser.contrasena)
            	user.first_name = newUser.nombre
            	user.save()
            	return HttpResponseRedirect("/"+respuesta)
    else:
        formulario = form()
    return render_to_response('aplicacion/formulario.html', {'formulario': formulario,
        'modelo': modelo, 'respuesta': respuesta}, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def parametrosIndex(request):
	listado = Parametro.objects.all()
	return render_to_response('aplicacion/parametros/index.html', {'parametros': listado},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarParametro(request):
	return agregar(request, ParametroForm, respuesta = "parametros", modelo = "Parametro")

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def verParametro(request, id):
	parametro = Parametro.objects.get(id=id)
	valores = ValorParametro.objects.filter(parametro=id)
	return render_to_response('aplicacion/parametros/detalle.html', {'parametro': parametro, 'valores': valores},
		context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u:u.is_staff, login_url='/login/')
def agregarValorParametro(request, id):
	parametro = Parametro.objects.get(id=id)
	valores = ValorParametro.objects.filter(parametro=id)
	if request.POST:
		form = ValorParametroForm(request.POST)
		if form.is_valid():
			valor = form.save(commit=False)
			valor.parametro = parametro
			valor.save()
			return HttpResponseRedirect("/parametros/"+str(id))
	else:
		form = ValorParametroForm()
	return render_to_response('aplicacion/parametros/detailform.html', {'formulario': form,
		'modelo': 'ValorParametro', 'respuesta': "'parametros/'+str(id)",
		 'parametro': parametro, 'valores': valores},
		 context_instance=RequestContext(request))


@login_required(login_url='/login/')
def eliminar(request, form, id, Model, respuesta, modelo):
	item = get_object_or_404(Model, id=id)
	if request.POST:
		formulario = form(request.POST, instance=item)
		if formulario.is_valid():
			item = formulario.save(commit=False)
			item.eliminado= True
			item.save()
			return HttpResponseRedirect("/"+respuesta)
	else:
		formulario = form(instance=item)
	return render_to_response('aplicacion/confirmacionEliminar.html', { 'modelo': modelo,
		'formulario': formulario, 'respuesta': respuesta },
		 context_instance=RequestContext(request))

@login_required(login_url='/login/')
def eliminarUsuario(request, id):
	return eliminar(request, eliminarUsuarioForm, id, Usuario, respuesta = "Usuario", modelo = "Usuario")

@login_required(login_url='/login/')
def eliminarcajaMenor(request, id):
	return eliminar(request, eliminarCajaMenorForm, id, CajaMenor, respuesta = "cajaMenor", modelo = "cajaMenor")
