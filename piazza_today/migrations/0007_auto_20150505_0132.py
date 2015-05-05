# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('piazza_today', '0006_auto_20150505_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenight',
            name='person',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gamenight',
            name='win_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='snitch',
            name='email_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snitch',
            name='person',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snitch',
            name='win_date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='aniversery',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
