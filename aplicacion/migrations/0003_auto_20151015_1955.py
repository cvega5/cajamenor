# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_auto_20151015_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='valorEnLetras',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
