from django.contrib import admin
from django.urls import path, include
from main.views import RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from debug_toolbar.toolbar import debug_toolbar_urls
from incident.urls import urlpatterns_incidents
from service.urls import urlpatterns_services


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/incidents/", include(urlpatterns_incidents)),
    path("api/services/", include(urlpatterns_services)),
] + debug_toolbar_urls()
