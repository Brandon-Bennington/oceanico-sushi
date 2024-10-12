from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        if self.parent_category:
            return f"{self.parent_category.name} -> {self.name}"
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=True, null=True)  # Quantity is optional
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        if self.category.parent_category:
            return f"{self.name} ({self.category.parent_category.name} -> {self.category.name})"
        return f"{self.name} ({self.category.name})"
