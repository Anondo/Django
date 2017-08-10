"""builtinViews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from genericView.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/$' , BooklistView.as_view(template_name = "booklist.html") , name = "books"),
    url(r'^book/(?P<pk>[0-9]+)/$' , BookDetailView.as_view(template_name = "book.html") , name = "book-detail"),
    url(r'^addbooks/$' , CreateBook.as_view() , name = "add_book"),
    url(r'^editbook/(?P<pk>[0-9]+)/$' , UpdateBook.as_view() , name = "edit_book")
]
