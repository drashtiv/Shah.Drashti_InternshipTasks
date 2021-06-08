from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Welcome...To home page of Django</h1>")

def aboutpage(request):
    return HttpResponse("<h1>Welcome...To about-us page of Django</h1>")

def contactpage(request):
    return HttpResponse("<h1>Welcome...To contact page of Django</h1>")
