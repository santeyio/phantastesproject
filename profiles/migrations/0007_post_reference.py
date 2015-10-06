# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reference',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
