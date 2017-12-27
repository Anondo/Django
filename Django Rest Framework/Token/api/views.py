from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

@api_view([ "GET"])
def get_token(request):
    username = request.GET.get('name')
    password = request.GET.get("pwd") #a very very bad practice to send confidential data by GET method

    user = authenticate(username = username , password = password)
    if not user:
        return Response({"Error": "Login Failed" , "username":username})
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
