# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0011_auto_20170924_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='texto',
            field=models.TextField(default='Default'),
        ),
    ]
