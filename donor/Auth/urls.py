from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('donor_login/',views.DonorLogIn, name='donor_login'),
    path('admin_login/',views.AdminLogIn, name='admin_login'),
    path('volunteer_login/',views.VolunteerLogIn, name='volunteer_login'),
    path('donor_reg/',views.Donor_reg, name='donor_reg'),
    path('logout/',views.LogOut, name='logout'),
    path('volunteer_reg/',views.volunteer_reg, name='volunteer_reg'),
    path('all_logins/',views.all_logins, name='all_logins'),
    path('donor_home/',views.donor_home, name='donor_home'),
    path('volunteer_home/',views.volunteer_home, name='volunteer_home'),
    path('admin_home/',views.admin_home, name='admin_home'),
    path('pending_donation/',views.pending_donation, name='pending_donation'),
    path('view_donationdetail/<int:pid>/',views.view_donationdetail, name='view_donationdetail'),
    path('donate_now/',views.donate_now, name='donate_now'),
    path('donation_history/',views.donation_history, name='donation_history'),
    path('accepted_donation/',views.accepted_donation, name='accepted_donation'),
    path('add_area/',views.add_area, name='add_area'),
    path('manage_area/',views.manage_area, name='manage_area'),
    path('edit_area/<int:pid>/',views.edit_area, name='edit_area'),
    path('delete_area/<int:pid>/',views.delete_area, name='delete_area'),
    path('manage_donor/',views.manage_donor, name='manage_donor'),
    path('view_donordetail/<int:pid>/',views.view_donordetail, name='view_donordetail'),
    path('view_volunteerdetail/<int:pid>/',views.view_volunteerdetail, name='view_volunteerdetail'),
    path('delete_donor/<int:pid>/',views.delete_donor, name='delete_donor'),
    path('new_volunteer/',views.new_volunteer, name='new_volunteer'),
    path('accepted_volunteer/',views.accepted_volunteer, name='accepted_volunteer'),
    path('rejected_volunteer/',views.rejected_volunteer, name='rejected_volunteer'),
    path('all_volunteer/',views.all_volunteer, name='all_volunteer'),
    path('delete_volunteer/<int:pid>/',views.delete_volunteer, name='delete_volunteer'),
    path('accepted_donationdetail/<int:pid>/',views.accepted_donationdetail, name='accepted_donationdetail'),
    path('collection_req/',views.collection_req, name='collection_req'),
    path('donationcollection_detail/<int:pid>/',views.donationcollection_detail, name='donationcollection_detail'),
    path('donationrec_volunteer/',views.donationrec_volunteer, name='donationrec_volunteer'),
    path('donationrec_detail/<int:pid>/',views.donationrec_detail, name='donationrec_detail'),
    path('donationnotrec_volunteer/',views.donationnotrec_volunteer, name='donationnotrec_volunteer'),
    path('donationdelivered_volunteer/',views.donationdelivered_volunteer, name='donationdelivered_volunteer'),
    path('profile_volunteer/',views.profile_volunteer, name='profile_volunteer'),

]