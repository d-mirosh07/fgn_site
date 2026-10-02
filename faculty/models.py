from django.db import models



class Department(models.Model):
    name=models.CharField(max_length=100)
    head=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=10)
    description=models.TextField()
    coordinator_name=models.CharField(max_length=100)
    coordinator_contact=models.CharField(max_length=100)
    disciplines=models.TextField(blank=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    degree=models.CharField(max_length=100,blank=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE,related_name='teachers')

    def __str__(self):
        return self.name

class FacultyInfo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    leadership=models.TextField(blank=True)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    instagram=models.URLField(blank=True)
    facebook=models.URLField(blank=True)

    def __str__(self):
        return self.title


class ExchangeProgram(models.Model):
    university=models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    languages = models.CharField(max_length=200)
    places = models.CharField(max_length=50)
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university