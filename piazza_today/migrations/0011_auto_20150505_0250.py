# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('piazza_today', '0010_auto_20150505_0247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventTypes',
            new_name='EventType',
        ),
        migrations.AlterField(
            model_name='teamevent',
            name='end_time',
            field=models.TimeField(default=datetime.time(2, 49, 58, 623795)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamevent',
            name='start_time',
            field=models.TimeField(default=datetime.time(2, 49, 58, 623770)),
            preserve_default=True,
        ),
    ]
