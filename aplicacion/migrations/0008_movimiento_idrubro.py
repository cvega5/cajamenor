# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_auto_20151104_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='idRubro',
            field=models.IntegerField(default=0),
        ),
    ]
