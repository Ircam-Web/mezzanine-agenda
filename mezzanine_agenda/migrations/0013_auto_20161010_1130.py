# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-10 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0012_auto_20161010_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='mentions_en',
            field=models.TextField(blank=True, null=True, verbose_name='mentions'),
        ),
        migrations.AddField(
            model_name='event',
            name='mentions_fr',
            field=models.TextField(blank=True, null=True, verbose_name='mentions'),
        ),
    ]