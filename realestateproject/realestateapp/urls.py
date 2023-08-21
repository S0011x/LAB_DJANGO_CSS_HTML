from django.contrib import admin
from django.urls import path
from realestateapp import views

app_name = 'realestateapp'
urlpatterns = [
    path('', views.home, name='home'),
    
]