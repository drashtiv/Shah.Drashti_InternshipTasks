from django.shortcuts import render
from django.http import HttpResponse

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
