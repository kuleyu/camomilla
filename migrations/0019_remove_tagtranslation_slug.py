# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0018_auto_20171127_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagtranslation',
            name='slug',
        ),
    ]
