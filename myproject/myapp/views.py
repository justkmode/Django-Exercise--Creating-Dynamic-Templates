# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

def menu(request):
    # Fetch all items from the Menu model
    menu_items = Menu.objects.all()
    
    # Create a dictionary to pass to the template
    items_dict = {'menu': menu_items}
    
    # Render the template with the menu items
    return render(request, 'menu.html', items_dict)
