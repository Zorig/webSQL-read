""" Card read admin """
from django.contrib import admin
from regist.models import RegisterStudent, Student_PersonalInfo
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
# Register your models here.


class RegisterStudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'time',)
    list_filter = ('student_id',)
    search_field = ('student_id',)


admin.site.register(RegisterStudent, RegisterStudentAdmin)
admin.site.register(Student_PersonalInfo)
