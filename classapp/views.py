from .models import Courses, MyCourse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Courses
from django.contrib import messages


# Create your views here.

def home(request):
    courses = Courses.objects.all()
    context = {'courses': courses}
    return render(request,'home.html', context)


def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    
    elif request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        u = User.objects.create(first_name= first_name,last_name= last_name ,username= username ,email= email)
        u.set_password(password)
        u.save()
        messages.success(request,'Registration SuccessFully..!')
        return redirect('/login')
    
    
def login_form(request):
    if request.method == 'GET':
        
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        
        u = authenticate(username = username ,password = password)
        
        if u is not None:
                login(request,u)
                return redirect('/')
        else:
            messages.success(request,'Enter valid detail..!')
            return redirect('/login')

def logout_page(request):
    logout(request) 
    return redirect("/login/")

def courses(request):

    courses = Courses.objects.all()

    context = {'courses': courses}

    return render(request, "courses.html", context)

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    
    elif request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        u = User.objects.create(first_name= first_name,last_name= last_name ,username= username ,email= email)
        u.set_password(password)
        u.save()
        messages.success(request,'Registration SuccessFully..!')
        return redirect('/login/')
    
    
def login_form(request):
    if request.method == 'GET':
        
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        
        u = authenticate(username = username ,password = password)
        
        if u is not None:
            login(request,u)
            return redirect('/')
        else:
            messages.success(request,'Enter valid detail..!')
            return redirect("/login/")

def logout_page(request):
    logout(request) 
    return redirect("/login/")

def buy_course(request, cid, uid):
    user = User.objects.get(id = uid)
    course = Courses.objects.get(id = cid)

    addCourse = MyCourse(user = user, course = course)
    addCourse.save()
    messages.success(request,'User added successfully !')
    return redirect('/')


def our_courses(request, uid):
    my_course = MyCourse.objects.filter(user = uid)

    context = {'courses': my_course}

    return render(request, "pricing.html", context)
