from django.urls import path
from . import views

app_name = 'menu'  # Add this line to create a namespace

urlpatterns = [
    path('', views.menu_list_view, name='list'),  # Changed 'menu-list' to 'list'
]