# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150917_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
