from django.shortcuts import render
from .models import *

def inventory(request):

    item = Item.objects.all()

    return render(request, 'inventory/views/inventory_list.html', {'item' : item})
