from django.shortcuts import render
from faculty.models import FacultyInfo, Program, Department
from django.http import Http404


def index(request):
    info=FacultyInfo.objects.first()
    return render(request, 'faculty/index.html', {'info': info})


def programs(request):
    all_programs = Program.objects.all()
    return render(request, 'faculty/programs.html', {'programs': all_programs})


def program(request, program_id):
    program = Program.objects.get(pk=program_id)
    return render(request, 'faculty/program.html', {'program': program})

def departments(request):
    all_departments = Department.objects.all()
    return render(request, 'faculty/departments.html', {'departments': all_departments})

def department(request, department_id):
    department = Department.objects.get(pk=department_id)
    return render(request, 'faculty/department.html', {'department': department})
