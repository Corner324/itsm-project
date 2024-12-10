from django.urls import path
from .views import ServiceListView, ServiceDetailView

urlpatterns_services = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
]