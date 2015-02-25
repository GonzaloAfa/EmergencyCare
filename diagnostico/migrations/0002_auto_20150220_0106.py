# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requerimientos',
            name='acceso_vascular',
            field=models.CharField(blank=True, max_length=20, choices=[(0, b'-'), (1, b'Periferico'), (2, b'Central')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='glasgow',
            field=models.CharField(blank=True, max_length=20, choices=[(0, b'-'), (1, b'14 - 15'), (2, b'9 - 13'), (3, b'0 - 8')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='hemodinamia',
            field=models.CharField(blank=True, max_length=20, choices=[(0, b'-'), (2, b'Estable'), (3, b'Inestable')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='oxigenoterapia',
            field=models.CharField(blank=True, max_length=20, choices=[(0, b'-'), (1, b'Naricera'), (2, b'Mascarilla Fio2 35-50%'), (3, b'Ventilacion Invasiva | No Invasiva')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='ventilatorio',
            field=models.CharField(blank=True, max_length=20, choices=[(0, b'-'), (1, b'Eupneico'), (2, b'Alterado')]),
            preserve_default=True,
        ),
    ]
