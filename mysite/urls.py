"""
Name: Rachel White
Class: Python Programming
Project: Mini Project 6 - Django Reading List

Root URL configuration. Sends app URLs to books.urls and uses Django's
built-in auth views for login and logout.
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("books.urls")),
]
