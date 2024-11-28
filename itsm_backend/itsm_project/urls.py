from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/catalog/', include('catalog.urls')),
    path('api/incidents/', include('incidents.urls')),
    path('api/messaging/', include('messaging.urls')),
]
