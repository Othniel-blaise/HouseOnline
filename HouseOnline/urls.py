from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    
    path('', views.login, name='login'),
    path('HouseOnline/', views.HouseOnline, name='HouseOnline'),
]
