from django.shortcuts import render
from faculty.models import FacultyInfo


def index(request):
    info=FacultyInfo.objects.first()
    return render(request, 'faculty/index.html', {'info': info})
