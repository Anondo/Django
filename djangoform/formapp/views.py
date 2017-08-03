from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

# Create your views here.


def index(request):
    person = Person.objects.all().order_by("-age")
    context = {
        "persons" : person,
    }
    return render(request , "index.html" , context)



def data_enter(request):
    form = PersonForm()
    context = {
        "form" : form,
    }
    return render(request , "form.html" , context)

def data_process(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        age = form.cleaned_data['age']
        person = Person(name = name , email=  email , age = age)
        person.save()
        return HttpResponse("<h1>Form submitted succesfully</h1>")
    else:
        return HttpResponse("<h1>Incorrect input</h1>")
