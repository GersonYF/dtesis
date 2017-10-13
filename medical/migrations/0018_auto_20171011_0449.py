# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0017_auto_20171011_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='rcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical.PuntajeCategoria'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medical.CategoriaPregunta'),
        ),
    ]
