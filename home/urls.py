from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/",views.loginUser, name="loginUser"),
    path("signup/", views.signupUser, name="signupUser"),
    path("logout/", views.logoutUser, name="logout"),


]


