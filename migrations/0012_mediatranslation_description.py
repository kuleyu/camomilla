# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0011_auto_20170325_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediatranslation',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
