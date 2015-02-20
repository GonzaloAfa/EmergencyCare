# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traslado',
            name='date_start',
        ),
        migrations.AddField(
            model_name='traslado',
            name='id_ficha',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
