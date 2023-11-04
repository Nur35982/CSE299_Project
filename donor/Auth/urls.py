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
    path('volunteer/',views.volunteer_info, name='volunteer'),
    path('all_logins/',views.all_logins, name='all_logins'),
    path('donor_home/',views.donor_home, name='donor_home'),
    path('admin_home/',views.admin_home, name='admin_home'),
    path('pending_donation/',views.pending_donation, name='pending_donation'),
    path('view_donationdetail/<int:pid>',views.view_donationdetail, name='view_donationdetail'),
    path('donate_now/',views.donate_now, name='donate_now'),
    path('donation_history/',views.donation_history, name='donation_history'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)