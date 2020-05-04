from django.contrib import admin
from django.urls import path, include
from .views import RegisterView,ShowUser, home, EntityAPIView, EntityDetails

urlpatterns = [
    path('register/',RegisterView),
    path('allusers/',ShowUser),
    path('',home),
    path('api-auth/', include('rest_framework.urls')),
    path('list-entities/', EntityAPIView.as_view()),
    path('entity/<int:id>/',EntityDetails.as_view()),
]