from django.shortcuts import render
from Auth.models import Volunteer

# Create your views here.

def SignIn(request):
    return render(request, 'Authentication/SignIn.html')

def SignUp(request):
    return render(request, 'Authentication/SignUp.html')

def volunteer_info(request):
    volunteer = Volunteer.objects.all()
    return render (request, 'Authentication/Volunteer.html', {'vlntr': volunteer})