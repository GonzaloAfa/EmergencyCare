# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monitorizacion', models.BooleanField(default=None)),
                ('ventilacion_mecanica', models.BooleanField(default=None)),
                ('inmovilizacion', models.BooleanField(default=None)),
                ('marcapaso', models.BooleanField(default=None)),
                ('BIC', models.CharField(max_length=20, blank=True)),
                ('oxigenoterapia', models.CharField(blank=True, max_length=20, choices=[(b'1', b'Naricera'), (b'2', b'Mascarilla Fio2 35-50%'), (b'3', b'Ventilacion Invasiva | No Invasiva')])),
                ('acceso_vascular', models.CharField(blank=True, max_length=20, choices=[(b'1', b'Periferico'), (b'2', b'Central')])),
                ('hemodinamia', models.CharField(blank=True, max_length=20, choices=[(b'1', b'Estable'), (b'2', b'Inestable')])),
                ('ventilatorio', models.CharField(blank=True, max_length=20, choices=[(b'1', b'Eupneico'), (b'2', b'Alterado')])),
                ('glasgow', models.CharField(blank=True, max_length=20, choices=[(b'1', b'14 - 15'), (b'2', b'9 - 13'), (b'3', b'0 - 8')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
