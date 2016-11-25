# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camomilla', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('read_article', 'Can read article'),)},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'permissions': (('read_category', 'Can read category'),), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'permissions': (('read_content', 'Can read content'),)},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'permissions': (('read_media', 'Can read media'),)},
        ),
        migrations.AlterModelOptions(
            name='sitemapurl',
            options={'permissions': (('read_sitemapurl', 'Can read sitemap url'),)},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'permissions': (('read_tag', 'Can read tag'),)},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('read_userprofile', 'Can read user profile'),)},
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
