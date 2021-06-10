from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Employee
from .models import Student

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

def signuppage(request):
    return render(request,'signup.html')

def loginpage(request):
    return render(request,'login.html')

def formpage(request):
    return render(request,'webform.html')

def process(request):
    print("welcome")
    print(request.method)
    print(request.POST)
    b = int(request.POST['txt1'])
    t = int(request.POST['txt2'])
    s = b + t
    print(s)

    return render(request,'answer.html',{'myb':b,'myt':t,'myans':s})

class employeelist(ListView):
    model = Employee
    template_name = 'emplist.html'

class studentlist(ListView):
    model = Student
    template_name = 'stdlist.html'