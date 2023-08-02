"""
Definition of views.
"""

#from datetime import datetime
from django.shortcuts import HttpResponse, render
#from django.http import HttpRequest

def home_page(request):
    return render(request, 'lists/home.html')

