from django.shortcuts import render, HttpResponse, redirect
from Auth.models import Donor
from .models import *
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import django.core.exceptions

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
    if request.method=='POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1 = Volunteer.objects.get(user=user)
                if user1.status != "pending":
                    login(request,user)
                    error = "no"
                else:
                    error = "not"
            except:
                error= "yes"
        else:
            error= "yes"
    return render(request, 'Authentication/VolunteerLogin.html', locals())

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

def volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    return render(request, 'Authentication/volunteer_home.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    return render(request, 'Authentication/admin_home.html')

def services(request):
    return render(request, 'Authentication/services.html')

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/DonorLogIn.html')
    user = request.user
    
    donor = Donor.objects.filter(user=user).first()
    error = None

    if request.method=="POST":
        donationname = request.POST['donationname']
        donationpic = request.FILES['donationpic']
        collectionloc = request.POST['collectionloc']
        description = request.POST['description']
        
        try:
            Donation.objects.create(donor=donor,donationname=donationname,donationpic=donationpic,collectionloc=collectionloc,description=description,status="pending")
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
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark'] 
        try:
            donation.adminremark = adminremark
            donation.status = status
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/view_donationdetail.html',locals())

def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    donation = Donation.objects.filter(status="accept")
    return render(request, 'Authentication/accepted_donation.html',locals())

def add_area(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    error = None

    if request.method=="POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        
        try:
            DonationArea.objects.create(areaname=areaname,description=description)
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/add_area.html',locals())

def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    area = DonationArea.objects.all()
    return render(request, 'Authentication/manage_area.html',locals())

def edit_area(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    area = DonationArea.objects.get(id=pid)
    error = None

    if request.method=="POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        area.areaname = areaname
        area.description = description
        try:
            area.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/edit_area.html',locals())

def delete_area(request,pid):
    DonationArea.objects.get(id=pid).delete()
    return render(request, 'Authentication/manage_area.html')

def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    donor = Donor.objects.all()
    return render(request, 'Authentication/manage_donor.html',locals())

def view_donordetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    donor = Donor.objects.get(id=pid)
    return render(request, 'Authentication/view_donordetail.html',locals())

def delete_donor(request,pid):
    User.objects.get(id=pid).delete()
    return render(request, 'Authentication/manage_donor.html')

def volunteer_reg(request):
    error =""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        address = request.POST['address']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        aboutme = request.POST['aboutme']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Volunteer.objects.create(user=user,contact=contact,address=address,userpic=userpic,idpic=idpic,aboutme=aboutme,status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'Authentication/volunteer_reg.html',locals())

def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    volunteer = Volunteer.objects.filter(status="pending")
    return render(request, 'Authentication/new_volunteer.html',locals())

def view_volunteerdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    volunteer = Volunteer.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark'] 
        try:
            volunteer.adminremark = adminremark
            volunteer.status = status
            volunteer.updationdate = date.today()
            volunteer.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/view_volunteerdetail.html',locals())

def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    volunteer = Volunteer.objects.filter(status="accept")
    return render(request, 'Authentication/accepted_volunteer.html',locals())

def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    volunteer = Volunteer.objects.filter(status="reject")
    return render(request, 'Authentication/rejected_volunteer.html',locals())

def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    volunteer = Volunteer.objects.all()
    return render(request, 'Authentication/all_volunteer.html',locals())

def delete_volunteer(request,pid):
    User.objects.get(id=pid).delete()
    return render(request, 'Authentication/all_volunteer.html')

def accepted_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/AdminLogIn.html')
    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()
    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid'] 
        da = DonationArea.objects.get(id=donationareaid)
        v = Volunteer.objects.get(id=volunteerid)
        try:
            donation.donationarea = da
            donation.volunteer = v
            donation.status = "Volunteer Allocated"
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/accepted_donationdetail.html',locals())

def collection_req(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer, status="Volunteer Allocated")
    return render(request, 'Authentication/collection_req.html',locals())

def donationcollection_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        volunteerremark = request.POST['volunteerremark'] 
        
        try:
            
            donation.status = status
            donation.volunteerremark = volunteerremark
            donation.updationdate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/donationcollection_detail.html',locals())

def donationrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer, status="Donation Received")
    return render(request, 'Authentication/donationrec_volunteer.html',locals())

def donationrec_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic'] 
        
        try:
            
            donation.status = status
            
            donation.updationdate = date.today()
            donation.save()
            Gallery.objects.create(donation=donation,deliverypic=deliverypic)
            error = "no"
        except:
            error = "yes"

    return render(request, 'Authentication/donationrec_detail.html',locals())

def donationnotrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer, status="Donation Not Received")
    return render(request, 'Authentication/donationnotrec_volunteer.html',locals())

def donationdelivered_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    user = request.user
    volunteer = Volunteer.objects.get(user = user)
    donation = Donation.objects.filter(volunteer = volunteer, status="Donation Delivered Successfully")
    return render(request, 'Authentication/donationdelivered_volunteer.html',locals())

def profile_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Authentication/VolunteerLogIn.html')
    error =""
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        address = request.POST['address']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        aboutme = request.POST['aboutme']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Volunteer.objects.create(user=user,contact=contact,address=address,userpic=userpic,idpic=idpic,aboutme=aboutme,status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'Authentication/profile_volunteer.html',locals())
