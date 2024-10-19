from django.shortcuts import render
from .models import MenuItem, Category

def menu_list_view(request):
    categories = Category.objects.filter(parent_category=None).order_by('order')
    menu_items_by_category = {}

    for category in categories:
        items = MenuItem.objects.filter(category=category).order_by('name')
        if items:
            menu_items_by_category[category] = items

        # Get items for subcategories
        subcategories = Category.objects.filter(parent_category=category)
        for subcategory in subcategories:
            subitems = MenuItem.objects.filter(category=subcategory).order_by('name')
            if subitems:
                if category not in menu_items_by_category:
                    menu_items_by_category[category] = []
                menu_items_by_category[category].extend(subitems)

    return render(request, 'menu/menu_list.html', {
        'menu_items_by_category': menu_items_by_category,
        'categories': categories
    })