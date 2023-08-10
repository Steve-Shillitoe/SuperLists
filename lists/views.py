"""
Definition of views.
"""

#from datetime import datetime
from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest
from lists.models import Item, List

def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.all(list=list_)
    return render(request, 'lists/list.html', {'items':items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')