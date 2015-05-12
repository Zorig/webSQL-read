# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0005_auto_20150414_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 14, 9, 43, 48, 485874), auto_now_add=True),
            preserve_default=True,
        ),
    ]
