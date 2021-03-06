# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('rating_count', models.IntegerField(default=0, editable=False)),
                ('rating_sum', models.IntegerField(default=0, editable=False)),
                ('rating_average', models.FloatField(default=0, editable=False)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_fr', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_fr', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('content_fr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('facebook_event', models.BigIntegerField(blank=True, null=True, verbose_name='Facebook')),
                ('allow_comments', models.BooleanField(default=False, verbose_name='Allow comments')),
                ('featured_image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Featured Image')),
                ('featured_image_description', models.TextField(blank=True, verbose_name='featured image description')),
                ('featured_image_header', mezzanine.core.fields.FileField(blank=True, max_length=1024, verbose_name='featured image header')),
                ('external_id', models.IntegerField(blank=True, null=True, verbose_name='external_id')),
                ('brochure', mezzanine.core.fields.FileField(blank=True, max_length=1024, verbose_name='brochure')),
                ('blog_posts', models.ManyToManyField(blank=True, related_name='events', to='blog.BlogPost', verbose_name='blog posts')),
            ],
            options={
                'verbose_name': 'Event',
                'ordering': ('start',),
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Event category',
                'verbose_name_plural': 'Event categories',
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('address', models.TextField()),
                ('mappable_location', models.CharField(blank=True, help_text='This address will be used to calculate latitude and longitude. Leave blank and set Latitude and Longitude to specify the location yourself, or leave all three blank to auto-fill from the Location field.', max_length=128)),
                ('lat', models.DecimalField(blank=True, decimal_places=7, help_text='Calculated automatically if mappable location is set.', max_digits=10, null=True, verbose_name='Latitude')),
                ('lon', models.DecimalField(blank=True, decimal_places=7, help_text='Calculated automatically if mappable location is set.', max_digits=10, null=True, verbose_name='Longitude')),
                ('featured_name', models.CharField(blank=True, max_length=512, null=True, verbose_name='featured name')),
                ('description', mezzanine.core.fields.RichTextField(blank=True, verbose_name='description')),
                ('description_fr', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('description_en', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='description')),
                ('link', models.URLField(blank=True, max_length=512, null=True)),
                ('external_id', models.IntegerField(blank=True, null=True, verbose_name='external_id')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Event Location',
                'ordering': ('title',),
                'verbose_name_plural': 'Event Locations',
            },
        ),
        migrations.CreateModel(
            name='EventPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='value')),
                ('unit', models.CharField(blank=True, max_length=16, null=True, verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'Event price',
                'ordering': ('-value',),
                'verbose_name_plural': 'Event pricies',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='mezzanine_agenda.EventCategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mezzanine_agenda.EventLocation'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='mezzanine_agenda.Event', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='event',
            name='prices',
            field=models.ManyToManyField(blank=True, related_name='events', to='mezzanine_agenda.EventPrice', verbose_name='prices'),
        ),
        migrations.AddField(
            model_name='event',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
