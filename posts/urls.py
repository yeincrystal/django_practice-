from django.contrib import admin
from django.urls import path
from . import views #import views from this directory 

urlpatterns = [
    path('', views.index,name="index"),
]
