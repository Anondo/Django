from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings(request):
    name = request.GET.get("name")
    if not name:
        name = "Unknown guy"
    context = {
        "name" : name,
    }
    return render(request , "greeting.html" , context)
