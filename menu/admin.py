from django.contrib import admin
from .models import MenuItem, Category

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_full_category', 'price', 'quantity', 'is_vegetarian')
    list_filter = ('category',)
    search_fields = ('name',)

    def get_full_category(self, obj):
        # Display the full category structure, including subcategory if applicable
        if obj.category.parent_category:
            return f"{obj.category.parent_category.name} -> {obj.category.name}"
        return obj.category.name

    get_full_category.short_description = 'Category'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'item_count')
    search_fields = ('name',)
    
    def item_count(self, obj):
        return obj.menuitem_set.count()
    item_count.short_description = 'Number of Items'

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)

