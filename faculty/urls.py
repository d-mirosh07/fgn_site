from django.urls import path
from faculty import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
    path('programs/<int:program_id>/', views.program, name='program'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:department_id>/', views.department, name='department'),
    path('exchange/', views.exchange, name='exchange'),
]