from django.urls import path
from .views import (
    IncidentCreateView,
    IncidentDetailView,
    MyIncidentsListView,
    AllIncidentsListView,
    IncidentUpdateView,
    PublicIncidentCreateView,
)

urlpatterns_incidents = [
    path("create/", IncidentCreateView.as_view(), name="incident-create"),
    path("my/", MyIncidentsListView.as_view(), name="my-incidents"),
    path("", AllIncidentsListView.as_view(), name="all-incidents"),
    path("<int:pk>/", IncidentDetailView.as_view(), name="incident-detail"),
    path("<int:pk>/update/", IncidentUpdateView.as_view(), name="incident-update"),
    path("public/create/", PublicIncidentCreateView.as_view(), name="public-incident-create"),
]
