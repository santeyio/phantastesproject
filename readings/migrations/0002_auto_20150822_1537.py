# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='description',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
