# -*- coding: utf-8 -*-
""" cardreader register model """
import datetime
from django.db import models
from regist import choices
# Create your models here.


class Student_PersonalInfo(models.Model):
    student_ID = models.CharField(max_length=10, default="1234567890")
    student_school_id = models.CharField(max_length=10, default="000000")
    lastname = models.CharField(max_length=20, default="last_name")
    firstname = models.CharField(max_length=20, default="student_name")
    student_class = models.CharField(max_length=3, default="11A")
    student_teacher = models.CharField(max_length=20, default=u"багш")
    student_class = models.CharField(max_length=3)
    gender = models.CharField(max_length=6, choices=choices.gender_choices)
    nationality = models.CharField(max_length=10, default="Халх")
    surname = models.CharField(max_length=20, null=True, blank=True)
    family = models.PositiveIntegerField(default=0)
    orphan = models.BooleanField(default=False)
    birthday = models.DateField()
    doc_id = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=11, default="AB-********")
    birthday_certificate_id = models.CharField(max_length=12, default="xxxxxxxx")
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    phone = models.CharField(max_length=10, help_text=u"Гэрийн утас", null=True, blank=True)
    address = models.CharField(max_length=160)
    father_name = models.CharField(max_length=30)
    father_status = models.CharField(max_length="20", help_text=u'Эцэгийн ажлын байдал')
    father_mobile = models.CharField(max_length=10)
    mother_name = models.CharField(max_length=30)
    mother_status = models.CharField(max_length="20", help_text=u'Эxийн ажлын байдал')
    mother_mobile = models.CharField(max_length=10)
    education_before_school = models.CharField(max_length=30)
    date_school = models.DateField()
    first_school = models.CharField(max_length=30)
    elementary_education_date = models.DateField()
    primary_education_date = models.DateField()
    primary_education_id = models.CharField(max_length=12)
    highschool_education_date = models.DateField()
    highschool_education_id = models.CharField(max_length=12)
    award = models.CharField(max_length=160, null=True, blank=True)
    interest = models.CharField(max_length=160, null=True, blank=True)
    eye_defect = models.CharField(max_length=50, null=True, blank=True)
    hearing_defect = models.CharField(max_length=50, null=True, blank=True)
    allergy = models.CharField(max_length=20, null=True, blank=True)
    chronic = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = "Хувийн мэдээлэл"
        verbose_name_plural = "Хувийн мэдээлэлүүд"

    def __unicode__(self):
        return self.student_ID


class RegisterStudent(models.Model):
    student_id = models.CharField(max_length=10, default="1234567890")
    time = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    take = models.BooleanField(default=False)
    dismiss = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.student_id
    
    class Meta:
        verbose_name = u'Бүртгэл'
        verbose_name_plural = u'Бүртгэл'
