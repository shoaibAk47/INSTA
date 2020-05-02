from django.contrib import admin
from django.urls import path
from .views import RegisterView,ShowUser, home

urlpatterns = [
    path('register/',RegisterView),
    path('allusers/',ShowUser),
    path('',home)
]