# Generated by Django 2.2.17 on 2021-12-15 12:47

from ..fields import JSONField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("camomilla", "0004_auto_20210511_0937"),
    ]

    operations = [
        migrations.AddField(
            model_name="media",
            name="image_props",
            field=JSONField(default=dict, blank=True),
        ),
    ]
