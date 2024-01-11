from collections.abc import Callable, Iterable, Mapping
from typing import Any
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#to activate thr user accounts
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import NoReverseMatch, reverse 
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str, DjangoUnicodeDecodeError

#getting tokens from utils.py
from .utils import TokenGenerator, generate_token



#for emails
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.core.mail import BadHeaderError,send_mail
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMessage

#for threading
import threading

class EmailThread(threading.Thread):

    def __init__(self,email_message):
        self.email_message=email_message
        threading.Thread.__init__()
    
    def run(self):
        self.email_message.send()



# Create your views here.

def signup(request):
 if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'auth/signup.html')
            
            
        try:
            if User.objects.get(username=email):


                messages.warning(request,"Email is Taken")
                return render(request,'auth/signup.html')

        except Exception as identifier:
            pass

        
        user = User.objects.create_user(email,email,password)
        user.first_name=first_name
        user.last_name=last_name
        user.is_active=False
        user.save()
        current_site=get_current_site(request)
        email_subject="Activate your Account"
        message=render_to_string('auth/activate.html',{
            'user':user,
            'domin':'http://127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)

        })

        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)

        EmailThread(email_message).start()
        messages.info(request,"Activate Your Account by clicking link on your email ")
        return redirect('/classauth/login')

 return render(request,'auth/signup.html')


class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=user.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.info(request,"Account Activated Successfully")
            return redirect('/classauth/login')
        return render(request,'auth/activatefail.html')



def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        user=authenticate(username=username,password=userpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Login Success")
            return render(request,'index.html')

        else:
            messages.error(request,"Invilid credentials")
            return redirect('/classauth/login/')
        
    return render(request,'auth/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/classauth/login/')
        