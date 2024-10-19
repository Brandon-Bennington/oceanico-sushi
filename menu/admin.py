from django.contrib import admin
from .models import MenuItem, Category

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_full_category', 'price', 'quantity', 'is_vegetarian')
    list_filter = ('category',)
    search_fields = ('name',)

    def get_full_category(self, obj):
        if obj.category.parent_category:
            return f"{obj.category.parent_category.name} -> {obj.category.name}"
        return obj.category.name

    get_full_category.short_description = 'Category'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'order', 'item_count')
    list_filter = ('parent_category',)
    search_fields = ('name',)
    ordering = ('order', 'name')  # This line ensures categories are ordered by 'order' field
    
    def item_count(self, obj):
        return MenuItem.objects.filter(category=obj).count()
    item_count.short_description = 'Number of Items'

    def get_queryset(self, request):
        # Override the default queryset to order by 'order' field
        return super().get_queryset(request).order_by('order', 'name')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)