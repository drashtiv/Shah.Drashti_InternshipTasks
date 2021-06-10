from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('about',views.aboutpage,name="about-us"),
    path('contact',views.contactpage,name="contact"),
    path('signup',views.signuppage,name="signup"),
    path('login',views.loginpage,name="login"),
    path('webform',views.formpage,name="webform"),
    path('formprocess',views.process,name="process"),
    path('emplist',views.employeelist.as_view(),name="employeelist"),
    path('stdlist',views.studentlist.as_view(),name="studentlist"),
]