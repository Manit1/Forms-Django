from django.shortcuts import render
from django.http import HttpResponseRedirect
from main import (
    forms,
    models
)
# Create your views here.

def index(request):
    context={
          'form':forms.Example
    }
    return render(request,'main/index.html',context)


def student(request):
    students = models.Student.objects.all()
    context={
        "students": students
    }
    return render(request,'main/student.html',context)

def addstudent(request):

    studentform = forms.StudentForm()
    if request.method == 'POST':
        studentform=forms.StudentForm(request.POST)
        if studentform.is_valid():
           student=studentform.save()
           return HttpResponseRedirect('/students')
    context={
        "studentform" : studentform
    }
    return render(request,'main/addstudent.html',context)