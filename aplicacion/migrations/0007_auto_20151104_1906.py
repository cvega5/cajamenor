# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_auto_20151016_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detmovimiento',
            name='movimiento',
        ),
        migrations.DeleteModel(
            name='DetMovimiento',
        ),
    ]
