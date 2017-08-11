from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Books

# Create your views here.

class BooklistView(generic.ListView): #the ListView is used for displaying object lists
    # the model and the context_object_name are the inherited attribtues of the ListView
    model = Books #sets the model and determiens which objects to display
    context_object_name = "books" #sets the context object name,by default it is set "object_list"

class BookDetailView(generic.DetailView):
    model = Books
    context_object_name = "book" #by default it is set, whatever the name of the model is in its lowercase i.e for this case it would have been books


class CreateBook(generic.CreateView):
    model = Books
    fields = ['name' , 'author' , 'genre' , 'price']

class UpdateBook(generic.UpdateView):
    model = Books
    fields = ['name' , 'author' , 'genre' , 'price']

class DeleteBook(generic.DeleteView):
    model = Books
    success_url = reverse_lazy("books")
