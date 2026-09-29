from django.urls import path
from faculty import views

urlpatterns = [
    path('', views.index, name='index'),
]