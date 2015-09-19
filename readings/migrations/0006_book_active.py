# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0005_auto_20150909_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
