""" Student registration form """
from django import forms
from regist.models import RegisterStudent, Student_PersonalInfo


class RegisterStudentForm(forms.ModelForm):

    class Meta:
        model = RegisterStudent
        fields = ['student_id']


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = Student_PersonalInfo
