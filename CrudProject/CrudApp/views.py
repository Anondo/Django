from django.shortcuts import render , redirect
from CrudApp.models import StudentInfo

# Create your views here.
def read(request):
    students = StudentInfo.objects.all().order_by("name")
    context = {
        "students" : students
    }
    return render(request , "read.html" , context)

def delete(request):
    print request.method
    students = StudentInfo.objects.all().order_by("name")
    context = {
        "students" : students
    }
    return render(request , "delete.html" , context)

def performDelete(request):
    studentName = request.GET.get("name")
    obj = StudentInfo.objects.get(name = studentName)
    obj.delete()
    return redirect(delete)

def create(request):
    return render(request , "create.html")

def performCreate(request):
    name = request.POST.get("name")
    age = int(request.POST.get("age"))
    institution = request.POST.get("institution")
    program = request.POST.get("program")
    bio = request.POST.get("bio")
    student = StudentInfo(name = name , age = age , institution = institution, program = program , bio = bio)
    student.save()
    return redirect(read)

def update(request):
    students = StudentInfo.objects.all().order_by("name")
    context = {
        "students" : students
    }
    return render(request , "update.html" , context)
def performUpdate(request):
    
