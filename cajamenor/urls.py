"""cajamenor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from aplicacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    url(r'^$', views.indexDefault),
    url (r'^admin/', include(admin.site.urls)),

    url (r'^usuarios/$', views.listaUsuarios),
    url(r'^nuevo/$', views.agregarUsuario),
    url(r'^usuarios/nuevo$', views.agregarUsuario),

    url(r'^Usuario/(?P<id>\d+)/$', views.editarUsuario),
    url(r'^usuarios/Usuario/(?P<id>\d+)/$', views.editarUsuario),
    url(r'^eliminarUsuario/(?P<id>\d+)/$', views.eliminarUsuario),

    url (r'^cajaMenor/$', views.listaCajaMenor),
    url (r'^nueva/$', views.agregarCajaMenor),
    url (r'^cajaMenor/nueva$', views.agregarCajaMenor),

    url(r'^editaCaja/(?P<id>\d+)/$', views.editarCajaMenor),
    url(r'cajaMenor/editaCaja/(?P<id>\d+)/$', views.editarCajaMenor),
    url(r'^eliminarcajaMenor/(?P<id>\d+)/$', views.eliminarcajaMenor),

    url(r'^movimientos/$', views.listaMovimientos),
    url(r'^nuevoMov/$', views.nuevoMovimiento),
    url(r'^movimientos/nuevoMov/$', views.nuevoMovimiento),

    url(r'^movimiento/(?P<id>\d+)/$', views.editarmovimiento),

    url(r'^$','aplicacion.views.indexDefault',name='incio'),

    url(r'^login/$','auten.views.login_view',name='vista_login'),
    url(r'^logout/$','auten.views.logout_view',name='vista_logout'),

    url(r'^parametros/$', 'aplicacion.views.parametrosIndex'),
    url(r'^parametros/add$', 'aplicacion.views.agregarParametro'),
    url(r'^parametros/(?P<id>\d+)/$', 'aplicacion.views.verParametro'),
    url(r'^parametros/(?P<id>\d+)/add-valor$', 'aplicacion.views.agregarValorParametro'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
