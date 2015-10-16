# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetMovimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rubro', models.CharField(max_length=40)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='cajamenor',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='eliminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cajamenor',
            name='totalDisponible',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='valorTransaccion',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='detmovimiento',
            name='movimiento',
            field=models.ForeignKey(to='aplicacion.Movimiento'),
        ),
    ]
