# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0004_auto_20150413_0923'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registerstudent',
            options={'verbose_name': '\u0411\u04af\u0440\u0442\u0433\u044d\u043b', 'verbose_name_plural': '\u0411\u04af\u0440\u0442\u0433\u044d\u043b'},
        ),
        migrations.AlterModelOptions(
            name='student_personalinfo',
            options={'verbose_name': '\u0425\u0443\u0432\u0438\u0439\u043d \u043c\u044d\u0434\u044d\u044d\u043b\u044d\u043b', 'verbose_name_plural': '\u0425\u0443\u0432\u0438\u0439\u043d \u043c\u044d\u0434\u044d\u044d\u043b\u044d\u043b\u04af\u04af\u0434'},
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='student_ID',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='student_class',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='student_school_id',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='student_teacher',
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='student_id',
            field=models.ForeignKey(related_name='student_info', default=b'1234567890', to='regist.Student_PersonalInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 14, 7, 31, 14, 333098), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student_personalinfo',
            name='firstname',
            field=models.CharField(default=b'student_name', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student_personalinfo',
            name='lastname',
            field=models.CharField(default=b'last_name', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student_personalinfo',
            name='student_ID',
            field=models.CharField(default=b'1234567890', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student_personalinfo',
            name='student_school_id',
            field=models.CharField(default=b'000000', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student_personalinfo',
            name='student_teacher',
            field=models.CharField(default='\u0431\u0430\u0433\u0448', max_length=20),
            preserve_default=True,
        ),
    ]
