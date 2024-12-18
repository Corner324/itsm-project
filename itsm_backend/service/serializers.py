from rest_framework import serializers
from .models import BusinessService, TechnicalService

class BusinessServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessService
        fields = ['id', 'category', 'name', 'description', 'status']

class TechnicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalService
        fields = ['id', 'category', 'name', 'configuration_items', 'status']
