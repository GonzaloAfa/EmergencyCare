# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0002_auto_20150218_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traslado',
            name='id_ficha',
        ),
    ]
