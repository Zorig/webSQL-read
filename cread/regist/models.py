# -*- coding: utf-8 -*-
""" cardreader register model """
import datetime
from django.db import models
from regist import choices
# Create your models here.


class Student_PersonalInfo(models.Model):
    student_ID = models.CharField(max_length=10, verbose_name=u"Сурагчын карт код")
    student_school_id = models.CharField(max_length=10, verbose_name=u'Сурагчын код')
    lastname = models.CharField(max_length=20, verbose_name=u"Овог")
    firstname = models.CharField(max_length=20, verbose_name=u"Нэр")
    student_class = models.CharField(max_length=3, null=True, blank=True, verbose_name=u"Анги")
    student_teacher = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"Багш")
    gender = models.CharField(max_length=6, choices=choices.gender_choices, verbose_name=u"Хүйс")
    nationality = models.CharField(max_length=10, default="Халх", verbose_name=u"Яс үндэс" )
    surname = models.CharField(max_length=20, null=True, blank=True, verbose_name="Ургийн овог")
    family = models.PositiveIntegerField(default=0, verbose_name=u"Ам бүл")
    orphan = models.BooleanField(default=False, verbose_name=u"Өнчин эсэх")
    birthday = models.DateField(verbose_name=u"Төрсөн он сар өдөр")
    doc_id = models.CharField(max_length=20, verbose_name=u"Хувийн хэргийн дугаар")
    registration_number = models.CharField(max_length=11, default="AB-********", verbose_name=u"Регистрийн дугаар")
    birthday_certificate_id = models.CharField(max_length=12, default="xxxxxxxx", verbose_name=u"Төрсний гэрчилгээний дугаар")
    email = models.EmailField(verbose_name=u"Имэйл")
    mobile = models.CharField(max_length=10, verbose_name=u"Гар утасны дугаар")
    phone = models.CharField(max_length=10, verbose_name=u"Гэрийн утас", null=True, blank=True)
    address = models.CharField(max_length=160, verbose_name=u"Гэрийн хаяг")
    father_name = models.CharField(max_length=30, verbose_name=u"Эцгийн нэр")
    father_status = models.CharField(max_length="20", verbose_name=u'Эцгийн ажлын байдал')
    father_mobile = models.CharField(max_length=10, verbose_name=u"Эцгийн утасны дугаар")
    mother_name = models.CharField(max_length=30, verbose_name=u"Эхийн нэр")
    mother_status = models.CharField(max_length="20", verbose_name=u'Эxийн ажлын байдал')
    mother_mobile = models.CharField(max_length=10, verbose_name=u"Эхийн утасны дугаар")
    education_before_school = models.CharField(max_length=30, verbose_name=u"Сургуулийн өмнөх боловсрол")
    date_school = models.DateField(verbose_name=u"Сургуульд элссэн он")
    first_school = models.CharField(max_length=30, verbose_name=u"Анх элссэн сургууль")
    elementary_education_date = models.DateField(verbose_name=u"Бага боловсрол эзэмшсэн он")
    primary_education_date = models.DateField(verbose_name=u"Дунд боловсрол эзэмшсэн он")
    primary_education_id = models.CharField(max_length=12, verbose_name=u"Дунд боловсрол эзэмшсэн сургууль")
    highschool_education_date = models.DateField(verbose_name=u"Ахлах боловсрол эзэмшсэн он")
    highschool_education_id = models.CharField(max_length=12, verbose_name=u"Ахлах боловсрол эзэмшсэн сургууль")
    award = models.CharField(max_length=160, null=True, blank=True, verbose_name=u"Авсан шагнал, медаль")
    interest = models.CharField(max_length=160, null=True, blank=True, verbose_name=u"Сонирхол хобби")
    eye_defect = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Нүдний хараа", default=u"Хэвийн")
    hearing_defect = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Сонсголын бэрхшээл", default=u"Хэвийн")
    allergy = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"Харшил")
    chronic = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"Архаг өвчин")

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
