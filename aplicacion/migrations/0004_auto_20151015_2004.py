# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20151015_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento',
            name='descripcionMo',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='descripcion',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
