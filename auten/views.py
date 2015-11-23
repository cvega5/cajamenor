from django.shortcuts import get_object_or_404, render_to_response
from django.template.defaulttags import csrf_token
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext
from django.http import HttpResponseRedirect
from auten.forms import LoginForm


def login_view(request):
    mensaje=""
    if request.user.is_authenticated() :
        return  HttpResponseRedirect('/')
    else:
        if request.method=="POST" :
            form=LoginForm(request.POST)
            if form.is_valid():
			    usuario = form.cleaned_data['usuario']
			    password = form.cleaned_data['password']
			    usuariov = authenticate(username=usuario,password=password)
			    if usuariov is not None and usuariov.is_active:
			        login(request,usuariov)
			        return HttpResponseRedirect('/')
			    else:
			        mensaje ="Usuario y/o Contrasena incorrecta"
        form =LoginForm()
        ctx={'form':form,'mensaje':mensaje}
        return render_to_response('auten/login.html',ctx,RequestContext(request))

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')
