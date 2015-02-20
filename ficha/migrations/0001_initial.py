# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('rut', models.CharField(max_length=12)),
                ('edad', models.IntegerField()),
                ('causa', models.CharField(max_length=30, choices=[(b'1', b'Examen'), (b'2', b'Traslado'), (b'3', b'Derivacion'), (b'4', b'Domicilio')])),
                ('diagnostico', models.TextField(null=True, blank=True)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('tipo_movil', models.CharField(max_length=30, choices=[(b'Normal', b'Basico'), (b'Medio', b'Mediana Complejidad'), (b'Alto', b'Alta Complejidad')])),
                ('responsable', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=13)),
                ('origen', models.CharField(max_length=120)),
                ('medico_derivador', models.CharField(max_length=60)),
                ('destino', models.CharField(max_length=120)),
                ('medico_receptor', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apodo', models.CharField(max_length=50)),
                ('patente', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado_ficha', models.CharField(max_length=30, choices=[(b'1', b'En lista'), (b'2', b'En Curso'), (b'3', b'Finalizado'), (b'4', b'Anulado')])),
                ('solicitud', models.CharField(max_length=30, verbose_name='Tipo de solicitud', choices=[(b'1', b'Programada'), (b'2', b'De inmediato')])),
                ('date_start', models.DateTimeField(auto_now=True)),
                ('hora_programada', models.DateTimeField(max_length=20, null=True, blank=True)),
                ('ficha', models.ForeignKey(to='ficha.Ficha')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Traslado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateTimeField(auto_now=True)),
                ('km_inicio', models.PositiveIntegerField(null=True, blank=True)),
                ('km_termino', models.PositiveIntegerField(null=True, blank=True)),
                ('inicio', models.DateTimeField(max_length=10, null=True, blank=True)),
                ('llegada', models.DateTimeField(max_length=10, null=True, blank=True)),
                ('inicio_espera', models.DateTimeField(max_length=10, null=True, blank=True)),
                ('termino_espera', models.DateTimeField(max_length=10, null=True, blank=True)),
                ('tiempo_espera', models.PositiveIntegerField(null=True, blank=True)),
                ('movil', models.ForeignKey(to='ficha.Movil')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servicio',
            name='traslado',
            field=models.ForeignKey(to='ficha.Traslado'),
            preserve_default=True,
        ),
    ]
