from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet
from django.urls import path
from .views import service_list

router = DefaultRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('services/', service_list, name='service_list'),
]