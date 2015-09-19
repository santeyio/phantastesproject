# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0006_book_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='schedule',
            new_name='book',
        ),
    ]
