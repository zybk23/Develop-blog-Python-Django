from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as authViews
from .views import *


app_name="users"

urlpatterns = [
    path("register/",RegisterView.as_view(),name="register"),
    path("login/",UserLogin.as_view(),name="login"),
    path("logout/",UserLogout.as_view(),name="logout"),
    path("password_change/",authViews.PasswordChangeView.as_view(),name="password_change"),
    path("password_change_done/",authViews.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('update_profile/<slug:slug>',UserProfileUpdateView.as_view(),name="update_profile"),
    path("my_profile/",UserProfileView.as_view(),name="myprofile")
]