""" Student registration form """
from django import forms
from regist.models import RegisterStudent, Student_PersonalInfo


class RegisterStudentForm(forms.ModelForm):

    class Meta:
        model = RegisterStudent


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = Student_PersonalInfo
