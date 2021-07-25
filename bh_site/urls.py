from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('flash_card/', include('flash_card.urls')),
    path('admin/', admin.site.urls),
]