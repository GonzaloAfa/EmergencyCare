# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0004_auto_20150224_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traslado',
            old_name='inicio',
            new_name='contacto_paciente',
        ),
        migrations.RenameField(
            model_name='traslado',
            old_name='inicio_espera',
            new_name='entrega_paciente',
        ),
        migrations.RenameField(
            model_name='traslado',
            old_name='llegada',
            new_name='fin_traslado',
        ),
        migrations.RenameField(
            model_name='traslado',
            old_name='termino_espera',
            new_name='inicio_traslado',
        ),
        migrations.RemoveField(
            model_name='traslado',
            name='tiempo_espera',
        ),
        migrations.AlterField(
            model_name='traslado',
            name='estado_traslado',
            field=models.CharField(max_length=20, choices=[(b'1', b'Salir de la base'), (b'2', b'Contacto con paciente'), (b'3', b'Inicio Traslado'), (b'4', b'Finaliza Traslado'), (b'5', b'Entrega del paciente')]),
            preserve_default=True,
        ),
    ]
