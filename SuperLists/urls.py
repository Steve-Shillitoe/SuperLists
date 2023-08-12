"""
Definition of urls for SuperLists.
"""

from django.urls import path, include
from django.contrib import admin
from lists import views as list_views
from lists import urls as list_urls


urlpatterns = [
    path('', list_views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('lists/', include(list_urls)),
   
]
