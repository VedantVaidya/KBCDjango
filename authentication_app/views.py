from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import *

def handellogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)
        if user is not None:
            request.session["uid"]=user.id
            login(request,user)
            messages.success(request,"Logged In Sucessfully")
            return redirect("/home")
        else:
            messages.success(request,"Invalid Details")
            return redirect("/")
    else:
        return render(request,'login.html')


def handellogout(request):
    logout(request)
    messages.success(request,"Logged Out Sucessfully")
    return redirect("/")

def handelsignup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        password=make_password(password)
        city=request.POST.get('city')
        state=request.POST.get('state')
        fullname=request.POST.get('name')
        obj=UserInfo(username=email,password=password,city=city,state=state,fullname=fullname)
        obj.save()
        messages.success(request,'Your Account was created Successfully!!!')
        return redirect("/")
    else:
        return render(request,'signup.html')