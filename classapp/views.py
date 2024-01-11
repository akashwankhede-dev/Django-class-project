from django.shortcuts import render
from .models import Courses

# Create your views here.

def home(request):
    return render(request,'home.html')


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,"signup.html")

def courses(request):

    courses = Courses.objects.all()

    context = {'cources': courses}

    return render(request, "courses.html", context)