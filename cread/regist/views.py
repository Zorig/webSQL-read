#! -*- coding:utf-8 -*-
""" Student registration view """
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from regist.models import RegisterStudent
from regist.forms import RegisterStudentForm, StudentInfoForm
# Create your views here.


def Register(request):
    registered_students = RegisterStudent.objects.all().order_by('-id')
    noon = datetime.time(12, 00, 00)
    a = datetime.datetime.now()
    a = a.time()
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            reg = form.save(commit=False)
            if a < noon:
                reg.take = True
            else:
                reg.dismiss = True
            reg.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterStudentForm()

    return render(request, 'reg.html', {'form': form, \
        'registered_students': registered_students})


@login_required
def reg_student(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reg')
    else:
        form = StudentInfoForm()
    return render(request, 'burtgel.html', {'form': form})
