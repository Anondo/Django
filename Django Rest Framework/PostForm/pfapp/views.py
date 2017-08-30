from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student
from .forms import StudentForm

class StudentRestView(APIView):


    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students , many = True)
        return Response(serializer.data)


class StudentPostView(View):
    template_name = "form.html"

    def get(self , request):
        context = {
            "form" : StudentForm(),
        }
        return render(request ,self.template_name ,  context)
    def post(self , request):
        serializer = StudentSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse("<h1>Done</h1>")
