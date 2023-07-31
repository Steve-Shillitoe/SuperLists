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
    path('login/',
         LoginView.as_view
         (
             template_name='lists/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
