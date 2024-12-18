from django.urls import path
from .views import (
    BusinessServiceListView,
    BusinessServiceDetailView,
    TechnicalServiceListView,
    TechnicalServiceDetailView
)

urlpatterns_services = [
    # Бизнес-каталог
    path('business/', BusinessServiceListView.as_view(), name='business-service-list'),
    path('business/<int:pk>/', BusinessServiceDetailView.as_view(), name='business-service-detail'),

    # Технический каталог
    path('technical/', TechnicalServiceListView.as_view(), name='technical-service-list'),
    path('technical/<int:pk>/', TechnicalServiceDetailView.as_view(), name='technical-service-detail'),
]