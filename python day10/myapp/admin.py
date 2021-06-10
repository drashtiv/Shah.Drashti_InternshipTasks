from django.contrib import admin

# Register your models here.

from .models import Employee
from .models import Student

admin.site.register(Employee)
admin.site.register(Student)
