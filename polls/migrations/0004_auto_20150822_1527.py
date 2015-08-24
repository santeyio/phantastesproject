# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_poll_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='nominations_open',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 22, 15, 27, 57, 539085, tzinfo=utc), verbose_name=b'date voting beings'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='notes',
            field=models.TextField(null=True, blank=True),
        ),
    ]
