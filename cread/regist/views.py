#! -*- coding:utf-8 -*-
""" Student registration view """
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from regist.models import RegisterStudent
from regist.forms import RegisterStudentForm, StudentInfoForm
# Create your views here.


def auth(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('regist.views.Register'))
            else:
                return HttpResponse(u'Гишүүнчлэл идэвхигүй байна')
        elif user.is_authenticated == True:
            return HttpResponseRedirect(reverse('regist.views.Register'))
        else:
            return HttpResponse(u'Нууц үг, нэвтрэх нэр буруу байна')
    return render(request, 'registration/login.html')


def Register(request):
    registered_students = RegisterStudent.objects.all()
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


def reg_student(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reg')
    else:
        form = StudentInfoForm()
    return render(request, 'burtgel.html', {'form': form})
