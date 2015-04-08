""" Card read admin """
from django.contrib import admin
from regist.models import RegisterStudent
# Register your models here.


class RegisterStudentAdmin(admin.ModelAdmin):
    list_display = ('student_ID',)
    list_filter = ('student_ID',)
    search_field = ('student_ID',)


admin.site.register(RegisterStudent, RegisterStudentAdmin)
