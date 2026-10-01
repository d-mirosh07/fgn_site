from django.contrib import admin
from faculty.models import Department, Program, Teacher, FacultyInfo, ExchangeProgram

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(FacultyInfo)
admin.site.register(ExchangeProgram)
