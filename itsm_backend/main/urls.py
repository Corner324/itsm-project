from django.urls import path
from .views import AdminDetailView, CurrentUserView, UserListView

urlpatterns_auth = [
    path("admin/", AdminDetailView.as_view(), name="admin-detail"),
    path('user/', CurrentUserView.as_view(), name='current-user'),
    path("users/", UserListView.as_view(), name="user-list"),
]
