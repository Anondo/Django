from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student

class StudentRestView(APIView):


    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students , many = True)
        return Response(serializer.data)

    def post(self , request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
