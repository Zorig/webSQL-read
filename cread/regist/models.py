# -*- coding: utf-8 -*-
""" cardreader register model """
from django.db import models
# Create your models here.


class RegisterStudent(models.Model):
    student_ID = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.student_ID

    class Meta:
        verbose_name = u'Оюутан'
        verbose_name_plural = u'Оюутнууд'
