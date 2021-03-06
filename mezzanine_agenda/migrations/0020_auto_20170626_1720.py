# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-06-26 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0019_auto_20170406_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('item_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Item URL')),
                ('pass_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pass URL')),
                ('confirmation_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Confirmation URL')),
            ],
            options={
                'verbose_name': 'Event shop',
                'verbose_name_plural': 'Event shops',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='mezzanine_agenda.EventShop', verbose_name='shop'),
        ),
    ]
