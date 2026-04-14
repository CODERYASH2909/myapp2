from django.shortcuts import render
from .models import Student

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        enroll=request.POST['enroll']
        email=request.POST['email']
        branch=request.POST['branch']

        Student.objects.create(
            name=name,
            enroll=enroll,
            email=email,
            branch=branch
        )

    return render(request,"home.html")