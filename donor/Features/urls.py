from django.urls import path
from .import views


urlpatterns = [
    path('cm/',views.Contact_Management, name='feature1'),
    path('dm/',views.Donor_Management, name='feature2'),

]