# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0003_auto_20150409_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_class', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=6, choices=[('\u042d\u0440', '\u042d\u0440\u044d\u0433\u0442\u044d\u0439'), ('\u042d\u043c', '\u042d\u043c\u044d\u0433\u0442\u044d\u0439')])),
                ('nationality', models.CharField(default=b'\xd0\xa5\xd0\xb0\xd0\xbb\xd1\x85', max_length=10)),
                ('surname', models.CharField(max_length=20, null=True, blank=True)),
                ('family', models.PositiveIntegerField(default=0)),
                ('orphan', models.BooleanField(default=False)),
                ('birthday', models.DateField()),
                ('doc_id', models.CharField(max_length=20)),
                ('registration_number', models.CharField(default=b'AB-********', max_length=11)),
                ('birthday_certificate_id', models.CharField(default=b'xxxxxxxx', max_length=12)),
                ('email', models.EmailField(max_length=75)),
                ('mobile', models.CharField(max_length=10)),
                ('phone', models.CharField(help_text='\u0413\u044d\u0440\u0438\u0439\u043d \u0443\u0442\u0430\u0441', max_length=10, null=True, blank=True)),
                ('address', models.CharField(max_length=160)),
                ('father_name', models.CharField(max_length=30)),
                ('father_status', models.CharField(help_text='\u042d\u0446\u044d\u0433\u0438\u0439\u043d \u0430\u0436\u043b\u044b\u043d \u0431\u0430\u0439\u0434\u0430\u043b', max_length=b'20')),
                ('father_mobile', models.CharField(max_length=10)),
                ('mother_name', models.CharField(max_length=30)),
                ('mother_status', models.CharField(help_text='\u042dx\u0438\u0439\u043d \u0430\u0436\u043b\u044b\u043d \u0431\u0430\u0439\u0434\u0430\u043b', max_length=b'20')),
                ('mother_mobile', models.CharField(max_length=10)),
                ('education_before_school', models.CharField(max_length=30)),
                ('date_school', models.DateField()),
                ('first_school', models.CharField(max_length=30)),
                ('elementary_education_date', models.DateField()),
                ('primary_education_date', models.DateField()),
                ('primary_education_id', models.CharField(max_length=12)),
                ('highschool_education_date', models.DateField()),
                ('highschool_education_id', models.CharField(max_length=12)),
                ('award', models.CharField(max_length=160, null=True, blank=True)),
                ('interest', models.CharField(max_length=160, null=True, blank=True)),
                ('eye_defect', models.CharField(max_length=50, null=True, blank=True)),
                ('hearing_defect', models.CharField(max_length=50, null=True, blank=True)),
                ('allergy', models.CharField(max_length=20, null=True, blank=True)),
                ('chronic', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='registerstudent',
            options={'verbose_name': '\u041e\u044e\u0443\u0442\u0430\u043d\u044b \u0435\u0440\u04e9\u043d\u0445\u0438\u0439 \u043c\u044d\u0434\u044d\u044d\u043b\u044d\u043b', 'verbose_name_plural': '\u041e\u044e\u0443\u0442\u043d\u0443\u0443\u0434\u044b\u043d \u0435\u0440\u04e9\u043d\u0445\u0438\u0439 \u043c\u044d\u0434\u044d\u044d\u043b\u044d\u043b'},
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='address',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='age',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='date',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='image',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='reg_ID',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='registerstudent',
            name='student_surname',
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='firstname',
            field=models.CharField(default=b'student_name', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='lastname',
            field=models.CharField(default=b'last_name', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='student_class',
            field=models.CharField(default=b'11A', max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='student_school_id',
            field=models.CharField(default=b'000000', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='registerstudent',
            name='student_teacher',
            field=models.CharField(default='\u0431\u0430\u0433\u0448', max_length=20),
            preserve_default=True,
        ),
    ]
