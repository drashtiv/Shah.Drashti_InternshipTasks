from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(default=False)
    salary = models.IntegerField()

    def __str__(self):
        return self.first_name

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrollment_no = models.IntegerField(default=False)
    email_id = models.EmailField()

    def __str__(self):
        return self.first_name

    