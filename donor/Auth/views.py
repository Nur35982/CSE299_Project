from django.shortcuts import render, HttpResponse, redirect
from Auth.models import Volunteer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def SignIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('Home/home.html')
        else:
            return HttpResponse("Username or Password is incorrect!")
    return render(request, 'Authentication/SignIn.html')

def SignUp(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your passsword and confirmation password are not same!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Authentication/SignIn.html')
    
    return render(request, 'Authentication/SignUp.html')

def LogOut(request):
    logout(request)
    return redirect('Authentication/LogIn.html')

def volunteer_info(request):
    volunteer = Volunteer.objects.all()
    return render (request, 'Authentication/Volunteer.html', {'vlntr': volunteer})

def all_logins(request):
    return render(request, 'Authentication/All_logins.html')