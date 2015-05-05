# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piazza_today', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='resturant',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
