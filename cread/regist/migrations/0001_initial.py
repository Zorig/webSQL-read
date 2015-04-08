# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_ID', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u041e\u044e\u0443\u0442\u0430\u043d',
                'verbose_name_plural': '\u041e\u044e\u0443\u0442\u043d\u0443\u0443\u0434',
            },
            bases=(models.Model,),
        ),
    ]
