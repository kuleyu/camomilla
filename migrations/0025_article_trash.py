# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-11-13 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0024_auto_20181004_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='trash',
            field=models.BooleanField(default=False),
        ),
    ]
