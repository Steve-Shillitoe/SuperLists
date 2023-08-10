"""
Definition of urls for SuperLists.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from lists import forms, views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('lists/<str:list_id>/', views.view_list, name='view_list'),
    path('lists/new', views.new_list, name='new_list'),
   
]
