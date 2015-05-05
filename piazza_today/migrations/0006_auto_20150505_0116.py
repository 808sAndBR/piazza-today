# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('piazza_today', '0005_meal_which_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthdate', models.DateField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='offline',
            name='date_leaving',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offline',
            name='date_returning',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offline',
            name='person',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
