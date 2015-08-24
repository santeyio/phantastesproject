# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150822_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='notes',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
