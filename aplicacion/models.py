from django.db import models
# Create your models here.
class Usuario(models.Model):
    identificacion = models.CharField(max_length = 15)
    nombre = models.CharField(max_length = 20, blank=True)
    apellido = models.CharField(max_length = 20, blank=True)
    contrasena = models.CharField(max_length = 20, blank=True)
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.identificacion

class CajaMenor(models.Model):
    nombreCaja = models.CharField(max_length=20)
    usuario = models.ForeignKey('Usuario')
    totalDisponible = models.DecimalField(max_digits=10, decimal_places=2)
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCaja

class Movimiento(models.Model):
    fecha = models.DateField()
    valorTransaccion = models.DecimalField(max_digits=10, decimal_places=2)
    valorEnLetras = models.CharField(max_length = 300, blank=True)
    descripcionMo = models.CharField(max_length = 200, blank=True)
    cajamenor = models.ForeignKey('CajaMenor')
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.valorTransaccion)

class DetMovimiento(models.Model):
    rubro = models.CharField(max_length = 40)
    movimiento = models.ForeignKey('Movimiento')
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.rubro


class Parametro(models.Model):
    atributo        =models.CharField(max_length=50)
    descripcion      =models.CharField(max_length=200)
    estadoParametro =models.CharField(max_length=1)

    def __str__(self):
        return self.atributo


class ValorParametro(models.Model):

    valor                =models.CharField(max_length=30)
    parametro            = models.ForeignKey('Parametro')
    orden                =models.CharField(max_length=3)
    estadoValorParametro =models.CharField(max_length=1)


    def __str__(self):
        return self.valor
