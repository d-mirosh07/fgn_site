from django.shortcuts import render
from faculty.models import FacultyInfo , Program


def index(request):
    info=FacultyInfo.objects.first()
    return render(request, 'faculty/index.html', {'info': info})


def programs(request):
    all_programs = Program.objects.all()
    return render(request, 'faculty/programs.html', {'programs': all_programs})


