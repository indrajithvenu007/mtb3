# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0022_remove_showmodel_s_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='showmodel',
            name='s_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='showmodel',
            name='s_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
