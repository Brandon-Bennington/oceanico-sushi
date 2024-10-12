from django.shortcuts import render
from .models import MenuItem, Category

def menu_list_view(request):
    categories = Category.objects.all()
    menu_items_by_category = {}

    for category in categories:
        items = MenuItem.objects.filter(category=category)
        if items:
            menu_items_by_category[category] = items

    return render(request, 'menu/menu_list.html', {'menu_items_by_category': menu_items_by_category})
