# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0008_auto_20170923_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='valor',
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='opciones',
            field=models.ManyToManyField(blank=True, to='medical.OpcionPregunta'),
        ),
    ]