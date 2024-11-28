from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer
from django.shortcuts import render

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

def service_list(request):
    return render(request, 'catalog/services.html')