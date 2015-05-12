# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0007_auto_20150415_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerstudent',
            name='dismiss',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='take',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 23, 8, 40, 6, 451275), auto_now_add=True),
            preserve_default=True,
        ),
    ]
