# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_post_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 0, 14, 23, 603383, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
