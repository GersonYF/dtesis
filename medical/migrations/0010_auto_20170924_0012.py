# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0009_auto_20170923_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(default='Categor\xeda', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='categoria',
            field=models.ManyToManyField(blank=True, to='medical.CategoriaPregunta'),
        ),
    ]
