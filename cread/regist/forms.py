""" Student registration form """
from django import forms
from regist.models import RegisterStudent


class RegisterStudentForm(forms.ModelForm):

    class Meta:
        model = RegisterStudent
        fields = ['student_ID']
