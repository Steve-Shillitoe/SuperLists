"""
Definition of views.
"""

#from datetime import datetime
from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'lists/home.html', {'items':items})

