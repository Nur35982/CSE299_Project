from django.shortcuts import render, HttpResponse, redirect
from Auth.models import Donor
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ValidationError
from django.db.utils import DatabaseError
import django.core.exceptions
from django.core.exceptions import FieldDoesNotExist
import os

# Create your views here.

def DonorLogIn(request):
    error = None
    if request.method=='POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error= "yes"
    return render(request, 'Authentication/DonorLogIn.html', locals())

def AdminLogIn(request):
    if request.method=='POST':
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error= "yes"
        except:
            error ="yes"
    return render(request, 'Authentication/AdminLogin.html', locals())

def VolunteerLogIn(request):
    return render(request, 'Authentication/VolunteerLogin.html')

def Donor_reg(request):
    error =""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        address = request.POST['address']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Donor.objects.create(user=user,contact=contact,userpic=userpic,address=address)
            error = "no"
        except:
            error = "yes"
    return render(request, 'Authentication/Donor_reg.html',locals())

def LogOut(request):
    logout(request)
    return redirect('home')

def volunteer_info(request):
    if 'q' in request.GET:
        q = request.GET['q']
        donor = Donor.objects.filter(first_name__icontains=q)
    else:
        donor = Donor.objects.all()
    context = {
        'donor': Donor
    }
    return render (request, 'Authentication/Volunteer.html', context)

def all_logins(request):
    return render(request, 'Authentication/All_logins.html')

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/DonorLogIn.html')
    return render(request, 'Authentication/donor_home.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/DonorLogIn.html')
    return render(request, 'Authentication/admin_home.html')

def services(request):
    return render(request, 'Authentication/services.html')

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/DonorLogIn.html')
    user = request.user
    
    donor = Donor.objects.get(user=user)

    if request.method=="POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']

        try:
            Donation.objects.create(donor=donor,donationpic=donationpic,collectionloc=collectionloc,description=description,status="pending")
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/donate_now.html',locals())

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/DonorLogIn.html')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'Authentication/donation_history.html',locals())

def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    donation = Donation.objects.filter(status="pending")
    return render(request, 'Authentication/pending_donation.html',locals())


def view_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    donation = Donation.objects.get(id=pid)
    return render(request, 'Authentication/view_donationdetail.html',locals())
