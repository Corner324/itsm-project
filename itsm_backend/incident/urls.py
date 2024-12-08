from django.urls import path
from .views import (
    IncidentCreateView,
    MyIncidentsListView,
    AllIncidentsListView,
    IncidentUpdateView,
)

urlpatterns = [
    path('create/', IncidentCreateView.as_view(), name='incident-create'),
    path('my/', MyIncidentsListView.as_view(), name='my-incidents'),
    path('', AllIncidentsListView.as_view(), name='all-incidents'),
    path('<int:pk>/', IncidentUpdateView.as_view(), name='incident-update'),
]
