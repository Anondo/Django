from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

class CustomView(View): #this is a class based view which is designed by the user not any built-in view(which django has plenty)
    template_name = "index.html"

    def get(self , request):
        return render(request , self.template_name)

    def post(self , request):
        name = request.POST.get("name")
        response = "<h1>Hello {}, this is it..goodbye!!</h1>".format(name)
        return HttpResponse(response)
