from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



#Employee signup details table
class Signup(models.Model):
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    re_password = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30, null=False)
    phone = models.IntegerField()

# Employee details table
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=30, null=False)
    emp_email = models.CharField(max_length=30, null=False, unique=True)
    emp_phone = models.IntegerField(null=False, unique=True)
    emp_role = models.CharField(max_length=30, null=False)
    dept_id = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    manager_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.manager_id}'

# Department details table
class Department(models.Model):
    dept_id = models.CharField(max_length=30, primary_key=True)
    dept_name = models.CharField(max_length=30, null=False)
    manager_id = models.IntegerField(null=True)
    dept_location = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.dept_id}'

# Client details table
class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    client_name = models.CharField(max_length=30, null=False)
    client_email = models.CharField(max_length=30, null=False)
    client_phone = models.IntegerField(null=False)
    client_alt_email = models.CharField(max_length=30, null=True)
    client_alt_phone = models.IntegerField(null=True)

#Project details table
class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=30, null=False)
    project_desc = models.CharField(max_length=200, null=False)
    project_budget = models.CharField(max_length=20, null=False)
    project_start_date = models.DateField(null=False)
    project_end_date = models.DateField(null=False)
    client_id = models.ForeignKey('Client',on_delete=models.CASCADE)
    dept_id = models.ForeignKey('Department',on_delete=models.CASCADE)