
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    enroll=models.CharField(max_length=20)
    email=models.EmailField()
    branch=models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
