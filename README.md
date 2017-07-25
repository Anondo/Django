# **Django In A Nutshell**

## **What Is Django:**
Django is a high-level python web framework which encourages rapid development with clean and pragmatic
design. Its main motto says it all: "The Web Framework For The Perfectionists With Deadlines". Django follows
the MVT(model-view-template) architectural pattern. Like it is said on the [Django website](https://www.djangoproject.com/) :
<br>

Ridiculously fast:

    Django was designed to help developers take applications from concept to completion as quickly as possible.
Reassuringly secure:

    Django takes security seriously and helps developers avoid many common security mistakes.
Exceedingly scalable:

    Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.



## **Installing Django:**
1. Go to your command prompt, for windows: cmd
1. pip install django (assuming you are a pythonista and you know how to use pip. If not,GOOGLE)
![installing django](https://github.com/Anondo/Django/blob/master/img/install.png)
1. Thats it!!
<hr>

## **Ready To GO With DjanGO:**
Here we will begin with the HelloProject project as our example.
#### **Creating The Project**
type "django-admin startproject HelloProject" from cmd
![creating project](https://github.com/Anondo/Django/blob/master/img/project.png)
This should create the HelloProject folder on your directory with the following structure:<br>
[HelloProject]/<br>
├── [HelloProject]/<br>
│   ├── __init__.py<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   └── wsgi.py<br>
└── manage.py<br>
This is the basic django project skeleton. Here:
1. __init__.py: this is the file that makes this folder a module(classic python!!)
1. settings.py: like the name says this file has got the settings for your project
1. urls.py: this file will contain all the mapping between the urls and the views.
1. wsgi.py: this file is if you want to deploy the project over WSGI
### **Creating The App**
A django project is nothing without its apps. Project are basically the summation of
some apps which are again reusable in other projects. So lets create our HelloApp:
type "cd HelloProject" to get inside the project. Here we will have the access to
manage.py. The manage.py is the local "django-admin" of the project or like its name
implies, is the manager of the project.
type "python manage.py startapp HelloApp" in the cmd
![creating app](https://github.com/Anondo/Django/blob/master/img/app.png)
This should create a HelloApp folder within our root project folder. Its skeleton should be like:<br>
HelloApp/<br>
   __init__.py<br>
   admin.py<br>
   models.py<br>
   tests.py<br>
   views.py<br>
1. __init__.py: you know what that is!
1. admin.py: to register our models as the admin
1. models.py: to create our models which are classes to be mapped with databases. Oh yea, django supports ORM(object-relation-mapping)
1. tests.py : to test our application
1. views.py: to create magic. I mean, to create the views which performs all the main application functions required for the website

To Be Conitnued....

<hr>
