""" Student registration view """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from regist.models import RegisterStudent
from regist.forms import RegisterStudentForm
# Create your views here.


def Register(request):
    registered_students = RegisterStudent.objects.all()
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reg')
    else:
        form = RegisterStudentForm()

    return render(request, 'reg.html', {'form': form, \
        'registered_students': registered_students})
