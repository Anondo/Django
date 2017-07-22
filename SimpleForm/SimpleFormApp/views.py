from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , "form.html")

def greet(request):
    name = request.POST.get("username")
    gender = request.POST.get("gender")
    print gender
    context = {
        "name" : name,
        "gender" : gender,
    }
    return render(request , "greet.html" ,context)
