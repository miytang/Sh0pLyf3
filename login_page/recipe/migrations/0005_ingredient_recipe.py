# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 23:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_ingredient_ingredient_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Recipe'),
            preserve_default=False,
        ),
    ]
