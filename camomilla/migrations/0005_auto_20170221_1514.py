# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-21 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0004_auto_20170119_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='og_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sitemapurl',
            name='og_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]
