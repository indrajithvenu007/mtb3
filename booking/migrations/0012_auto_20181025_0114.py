# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20181023_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='ticket_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.ScreenModel'),
        ),
    ]
