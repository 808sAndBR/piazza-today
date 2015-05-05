# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piazza_today', '0004_auto_20150504_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='which_meal',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
