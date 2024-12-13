from rest_framework import generics
from .models import BusinessService, TechnicalService
from .serializers import BusinessServiceSerializer, TechnicalServiceSerializer
from rest_framework.permissions import IsAuthenticated

# Бизнес-каталог
class BusinessServiceListView(generics.ListCreateAPIView):
    queryset = BusinessService.objects.all()
    serializer_class = BusinessServiceSerializer
    permission_classes = [IsAuthenticated]

class BusinessServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessService.objects.all()
    serializer_class = BusinessServiceSerializer
    permission_classes = [IsAuthenticated]

# Технический каталог
class TechnicalServiceListView(generics.ListCreateAPIView):
    queryset = TechnicalService.objects.all()
    serializer_class = TechnicalServiceSerializer
    permission_classes = [IsAuthenticated]

class TechnicalServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnicalService.objects.all()
    serializer_class = TechnicalServiceSerializer
    permission_classes = [IsAuthenticated]
