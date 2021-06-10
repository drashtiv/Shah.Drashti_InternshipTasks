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
