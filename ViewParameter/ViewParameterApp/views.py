from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request , year):
    age = int(datetime.datetime.now().year)
    return HttpResponse("<h1>So your age is   {}</h1>".format(age - int(year)))
