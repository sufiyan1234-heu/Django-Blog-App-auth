from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [

    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("signup/", views.signupUser, name='signup'),

]
