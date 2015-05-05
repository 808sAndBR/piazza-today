# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piazza_today', '0002_meal_resturant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='resturant',
            new_name='meal',
        ),
    ]
