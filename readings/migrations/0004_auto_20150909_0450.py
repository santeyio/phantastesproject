# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_auto_20150909_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='date',
        ),
        migrations.AddField(
            model_name='day',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
