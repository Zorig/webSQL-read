# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0006_auto_20150414_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerstudent',
            name='student_id',
            field=models.CharField(default=b'1234567890', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 15, 8, 18, 54, 747308), auto_now_add=True),
            preserve_default=True,
        ),
    ]
