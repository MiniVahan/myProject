from django.shortcuts import render
from .models import Student
from .forms import AddStudentForm, SearchStudentForm, DeleteStudentForm, UpdateStudentForm


def index(request):
    return render(request, 'base.html')


def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students':students})


def add_student(request):
    form = AddStudentForm()
    info = None
    if request.method == 'POST':
        Student.objects.create(name=request.POST.get('name'),
                               surname=request.POST.get('surname'),
                               age=request.POST.get('age'),
                               )
        info = 'Student successfully added into database '
    return render(request, 'students.html', {'form': form, 'info': info})


def search_student(request):
    form = SearchStudentForm()
    student = None
    info = None
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            student = Student.objects.get(name=name)
        except Student.DoesNotExist:
            student = None
            info = 'There is no such student. Please check the name and enter again'
    return render(request, 'students.html', {'form': form, 'student': student, 'info':info})


def update_student(request):
    form = UpdateStudentForm()
    student = None
    info = None
    if request.method == 'POST':
        old_name = request.POST.get('old_name')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        student = Student.objects.get(name=old_name)
        student.name = name
        student.surname = surname
        student.age = age
        student.save()
        info = 'Student info has been updated'
    return render(request, 'students.html', {'form': form, 'info': info})


def delete_student(request):
    form = DeleteStudentForm()
    info = None
    if request.method == 'POST':
        name = request.POST.get('name')
        all_students = Student.objects.all()
        entry = Student.objects.get(name=name)
        entry.delete()
        for student in all_students:
            if name == student.name:
                info = 'Student deleted from database'
                break
            else:
                info = 'No such Student'
    return render(request, 'students.html', {'form': form, 'info': info})
