# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 03:44
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamomillaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('level', models.CharField(choices=[('1', 'Guest'), ('2', 'Editor'), ('3', 'Admin')], default='1', max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('read_userprofile', 'Can read user profile'),),
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PUB', 'Published'), ('DRF', 'Draft'), ('TRS', 'Trash')], default='DRF', max_length=3)),
                ('date', models.DateTimeField(auto_now=True)),
                ('og_image', models.URLField(blank=True, default='', null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('read_article', 'Can read article'),),
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('permalink', models.CharField(max_length=200)),
                ('og_description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('og_title', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('og_type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('og_url', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('canonical', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Article')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'camomilla_article_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('read_category', 'Can read category'),),
                'abstract': False,
                'verbose_name_plural': 'categories',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Category')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'camomilla_category_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PUB', 'Published'), ('DRF', 'Draft'), ('TRS', 'Trash')], default='DRF', max_length=3)),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('read_content', 'Can read content'),),
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('content', models.TextField()),
                ('permalink', models.CharField(max_length=200)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Content')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'camomilla_content_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('thumbnail', models.ImageField(blank=True, max_length=500, null=True, upload_to='thumbnails')),
                ('created', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.IntegerField(blank=True, default=0, null=True)),
                ('is_image', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('read_media', 'Can read media'),),
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MediaTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Media')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'camomilla_media_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SitemapUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=200, unique=True)),
                ('og_image', models.URLField(blank=True, default='', null=True)),
            ],
            options={
                'permissions': (('read_sitemapurl', 'Can read sitemap url'),),
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SitemapUrlTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('permalink', models.CharField(max_length=200)),
                ('og_description', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('og_title', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('og_type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('og_url', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('canonical', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.SitemapUrl')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'camomilla_sitemapurl_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('read_tag', 'Can read tag'),),
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_plain_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TagTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='camomilla.Tag')),
            ],
            options={
                'default_permissions': (),
                'db_table': 'camomilla_tag_translation',
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='content',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camomilla.SitemapUrl'),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='camomilla.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='highlight_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='camomilla.Media'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='camomilla.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='tagtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='sitemapurltranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='mediatranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('permalink', 'language_code'), ('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('permalink', 'language_code'), ('language_code', 'master')]),
        ),
    ]
