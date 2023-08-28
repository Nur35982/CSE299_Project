from django.urls import path
from .import views


urlpatterns = [
    path('signin/',views.SignIn, name='signin'),
    path('signup/',views.SignUp, name='signup'),
    path('logout/',views.LogOut, name='logout'),
    path('volunteer/',views.volunteer_info, name='volunteer'),
    path('all_logins/',views.all_logins,name='all_logins'),

]