from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Root URL pointing to pages.urls
    path('menu/', include('menu.urls')),  # Menu URL pointing to menu.urls
]
