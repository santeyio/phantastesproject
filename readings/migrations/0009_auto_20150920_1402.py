# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0008_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='book',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
    ]
