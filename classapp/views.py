from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')


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