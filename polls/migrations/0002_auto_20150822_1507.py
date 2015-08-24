# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='due_date',
        ),
        migrations.AddField(
            model_name='poll',
            name='voting_close',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 22, 15, 7, 28, 100905, tzinfo=utc), verbose_name=b'date voting closes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='voting_open',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 22, 15, 7, 34, 655350, tzinfo=utc), verbose_name=b'date voting beings'),
            preserve_default=False,
        ),
    ]
