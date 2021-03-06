# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='category',
        ),
        migrations.RemoveField(
            model_name='event',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='featured_image_description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='featured_image_header',
        ),
        migrations.AddField(
            model_name='event',
            name='sub_title',
            field=models.TextField(blank=True, max_length=1024, verbose_name='sub title'),
        ),
        migrations.DeleteModel(
            name='EventCategory',
        ),
    ]
