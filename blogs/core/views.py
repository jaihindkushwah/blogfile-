
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import blog


# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def blog_page(request):
    blogs=blog.objects.all()
    # return render(request,'blog_page.html',{'body_words': body_words})
    return render(request,'blog_page.html',{'blogs':blogs})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,'This email is already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'This username is in used , Please choose another')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'You have registered successfully!')
                return redirect('login')
        else:
            messages.info(request,'Password not matched')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('index')

from django.http import HttpResponse
from django.template import loader

def forget(request):
    return render(request,'forget.html')


