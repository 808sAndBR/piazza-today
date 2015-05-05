# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('piazza_today', '0008_teamevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamevent',
            name='end_time',
            field=models.TimeField(default=datetime.time(2, 40, 13, 806325)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teamevent',
            name='start_time',
            field=models.TimeField(default=datetime.time(2, 40, 13, 806283)),
            preserve_default=True,
        ),
    ]
