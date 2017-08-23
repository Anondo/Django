from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 180)
    author = serializers.CharField(max_length = 120)
    genre = serializers.CharField(max_length = 30)
    price  = serializers.FloatField()

    def create(self , validated_data):
        return Book.objects.create(**validated_data)
