# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerstudent',
            name='time',
        ),
        migrations.AlterField(
            model_name='registerstudent',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
