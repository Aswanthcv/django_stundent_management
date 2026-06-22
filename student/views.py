from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):

  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    course = request.POST.get('course')

    students = Students (
      name=name,
      email=email,
      course=course
    )
    students.save()

  students = Students.objects.all()

  context = {
    'students':students,
    'status_choice':STATUS_CHOICES
  }

  return render(request,'home.html',context)



def delete_student(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect('home')

def update_student(request, id):
   student = Students.objects.get(id=id)
   if request.method == 'POST':
      student.name = request.POST.get('name')
      student.email = request.POST.get('email')
      student.course = request.POST.get('course')
      
      student.save()
      return redirect('home')
   
   context = {
      'student' : student
   }
   return render(request,'update.html',context)