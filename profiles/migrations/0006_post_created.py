# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20151002_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 6, 15, 24, 23, 466426, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
