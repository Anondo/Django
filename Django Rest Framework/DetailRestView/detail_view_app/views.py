from django.shortcuts import render , redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Account
from .serializers import AccountSerializer


class AccountsRestView(APIView):

    def get(self,request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts , many = True)
        return Response(serializer.data)

    def post(self , request):
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailView(APIView):

    def get(self , request , pk):
        account = Account.objects.get(pk = pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    def put(self , request , pk): #to update
        account = Account.objects.get(pk = pk)
        serializer = AccountSerializer(account , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    def delete(self , request , pk): #to delete
        account = Account.objects.get(pk = pk)
        account.delete()
        return redirect("accounts")
