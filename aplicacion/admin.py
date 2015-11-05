from django.contrib import admin
from aplicacion.models import *
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id','identificacion','nombre','apellido')

class CajaMenorAdmin(admin.ModelAdmin):
    list_display=('id','nombreCaja','usuario','totalDisponible')

class MovimientoAdmin(admin.ModelAdmin):
    list_display=('id','fecha','valorEnLetras','valorTransaccion','descripcion','idRubro','cajamenor')

class ParametroAdmin(admin.ModelAdmin):
    list_display=('id','atributo','descripcion','estadoParametro')

class ValorParametroAdmin(admin.ModelAdmin):
    list_display=('id','valor','parametro','orden','estadoValorParametro')



admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(CajaMenor,CajaMenorAdmin)
admin.site.register(Movimiento,MovimientoAdmin)
admin.site.register(Parametro,ParametroAdmin)
admin.site.register(ValorParametro,ValorParametroAdmin)
