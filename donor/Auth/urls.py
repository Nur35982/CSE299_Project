from django.urls import path
from .import views


urlpatterns = [
    path('signin/',views.SignIn, name='signin'),
    path('signup/',views.SignUp, name='signup'),
    path('volunteer/',views.volunteer_info),

]