from django.urls import path
from .import views


urlpatterns = [
    path('blg/',views.blog, name='blog'),

]