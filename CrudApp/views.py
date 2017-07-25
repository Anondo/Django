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
    students = StudentInfo.objects.all().order_by("name")
    context = {
        "students" : students
    }
    return render(request , "delete.html" , context)

def performDelete(request):
    key = request.GET.get("key")
    obj = StudentInfo.objects.get(pk = key)
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
    key = request.GET.get("key")
    newName = request.POST.get("name")
    newAge = request.POST.get("age")
    newInstitution = request.POST.get("institution")
    newProgram = request.POST.get("program")
    newBio = request.POST.get("bio")
    student = StudentInfo.objects.get(pk = key)
    if(newName != ""):
        student.name = newName
    if(newAge != ""):
        student.age = int(newAge)
    if(newInstitution != ""):
        student.institution = newInstitution
    if(newProgram != ""):
        student.program = newProgram
    if(newBio != ""):
        student.bio = newBio
    student.save()
    return redirect(update)
