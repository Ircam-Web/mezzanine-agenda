# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0004_auto_20160907_1046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'verbose_name': 'Event category', 'verbose_name_plural': 'Event categories'},
        ),
    ]
