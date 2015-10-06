# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readings', '0009_auto_20150920_1402'),
        ('profiles', '0004_auto_20151001_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='underline',
            name='book',
        ),
        migrations.RemoveField(
            model_name='underline',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='book',
            field=models.ForeignKey(blank=True, to='readings.Book', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='underline', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Underline',
        ),
        migrations.AddField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(to='profiles.Post'),
        ),
        migrations.AddField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(to='profiles.Post'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
