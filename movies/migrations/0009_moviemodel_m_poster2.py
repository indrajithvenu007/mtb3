# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-14 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20181014_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='m_poster2',
            field=models.ImageField(default='Pictures/ranam.jpg', upload_to='media/movie_posters_covers', verbose_name='Movie Poster cover'),
        ),
    ]