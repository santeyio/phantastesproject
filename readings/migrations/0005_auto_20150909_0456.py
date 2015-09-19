# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0004_auto_20150909_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='order',
            new_name='day',
        ),
    ]
