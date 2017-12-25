from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Subscriber
from .serializers import SubscriberSerializer


#ViewSets is what the name suggests is a class which is a set of view
#with APIView we needed multiple classes for list , list details , create etc.
#but with ViewSets, we need only one class to handle all kinds of request
#the http verbs i.e the methods of the ViewSets are list , retrieve , create , update instead of post,get,put,patch
class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
