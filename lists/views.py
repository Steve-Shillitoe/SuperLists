"""
Definition of views.
"""

#from datetime import datetime
from django.shortcuts import HttpResponse, render
from django.http import HttpRequest
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''
    
    return render(request, 'lists/home.html', {
        'new_item_text':new_item_text})

