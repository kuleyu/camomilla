# Generated by Django 2.2.3 on 2019-09-11 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0002_auto_20190911_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletranslation',
            name='content_title',
        ),
    ]