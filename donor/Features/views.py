from django.shortcuts import render

# Create your views here.

def Contact_Management(request):
    return render(request, 'Features/Contact_Management.html')

def Donor_Management(request):
    return render(request, 'Features/Donor_Management.html')