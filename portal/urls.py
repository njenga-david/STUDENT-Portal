from django.urls import path
from django import http
from . import views



urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('',views.homePage,name='home'),


]