"""
Definition of views.
"""

#from datetime import datetime
from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest
from lists.models import Item

def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items':items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')