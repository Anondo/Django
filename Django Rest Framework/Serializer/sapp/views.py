from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
# Create your views here.

@api_view(['GET'])
def Books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books , many = True)
    return Response(serializer.data)
