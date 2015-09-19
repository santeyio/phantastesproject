# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20150822_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='votes',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='nominations_open',
            field=models.DateTimeField(verbose_name=b'Date nominations open'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date created'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='voting_close',
            field=models.DateTimeField(verbose_name=b'Date voting closes'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='voting_open',
            field=models.DateTimeField(verbose_name=b'Date voting begins'),
        ),
    ]
