# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('readings', '0009_auto_20150920_1402'),
        ('profiles', '0003_auto_20150930_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Underline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField()),
                ('book', models.ForeignKey(to='readings.Book')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='book',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
