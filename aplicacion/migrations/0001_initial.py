# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CajaMenor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreCaja', models.CharField(max_length=20)),
                ('totalDisponible', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('valorTransaccion', models.IntegerField()),
                ('valorEnLetras', models.CharField(max_length=30, blank=True)),
                ('descripcionMo', models.CharField(max_length=200, blank=True)),
                ('cajamenor', models.ForeignKey(to='aplicacion.CajaMenor')),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('estadoParametro', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=20, blank=True)),
                ('apellido', models.CharField(max_length=20, blank=True)),
                ('contrasena', models.CharField(max_length=20, blank=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ValorParametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=30)),
                ('orden', models.CharField(max_length=3)),
                ('estadoValorParametro', models.CharField(max_length=1)),
                ('parametro', models.ForeignKey(to='aplicacion.Parametro')),
            ],
        ),
        migrations.AddField(
            model_name='cajamenor',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
    ]
