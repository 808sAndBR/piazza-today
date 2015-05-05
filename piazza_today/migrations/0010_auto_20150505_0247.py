# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('piazza_today', '0009_auto_20150505_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('celibration', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teamevent',
            name='event_type',
            field=models.ForeignKey(default=1, to='piazza_today.EventTypes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teamevent',
            name='end_time',
            field=models.TimeField(default=datetime.time(2, 47, 41, 8275)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamevent',
            name='start_time',
            field=models.TimeField(default=datetime.time(2, 47, 41, 8254)),
            preserve_default=True,
        ),
    ]
