# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0003_remove_traslado_id_ficha'),
    ]

    operations = [
        migrations.AddField(
            model_name='traslado',
            name='estado_traslado',
            field=models.CharField(default='1', max_length=20, choices=[(b'0', b'Sin movimiento'), (b'1', b'Contacto con paciente'), (b'2', b'Inicio Traslado'), (b'3', b'Finaliza Traslado'), (b'4', b'Entrega del paciente')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ficha',
            name='tipo_movil',
            field=models.CharField(max_length=30, choices=[(b'Normal', b'Complejidad Baja'), (b'Medio', b'Complejidad Mediana '), (b'Alto', b'Complejidad Alta ')]),
            preserve_default=True,
        ),
    ]
