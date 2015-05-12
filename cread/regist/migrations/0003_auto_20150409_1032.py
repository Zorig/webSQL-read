# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0002_auto_20150401_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerstudent',
            name='address',
            field=models.CharField(default=b'_', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='age',
            field=models.IntegerField(default=b'6'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='image',
            field=models.ImageField(null=True, upload_to=b'studentImage', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='reg_ID',
            field=models.CharField(default=b'AB-XXXXXXXX', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='student_name',
            field=models.CharField(default=b'AB', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='student_surname',
            field=models.CharField(default=b'AB', max_length=20),
            preserve_default=True,
        ),
    ]
