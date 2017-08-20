from django.shortcuts import render
from django.views import generic

from .models import Employee
# Create your views here.

class EmployeeList(generic.ListView):
    model = Employee
    context_object_name = "employees"

class EmployeeDetail(generic.DetailView):
    model = Employee
    context_object_name = "employee"
