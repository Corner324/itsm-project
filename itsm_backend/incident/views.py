from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Incident
from .serializers import IncidentSerializer, IncidentUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework import serializers
from rest_framework import status

class IncidentCreateView(generics.CreateAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MyIncidentsListView(generics.ListAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(created_by=self.request.user)

class AllIncidentsListView(generics.ListAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'support': # type: ignore
            raise PermissionError("У вас нет прав для просмотра всех заявок.")
        return Incident.objects.all()

class IncidentUpdateView(generics.UpdateAPIView):
    serializer_class = IncidentUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'support': # type: ignore
            raise PermissionError("Вы не можете обновлять заявки.")
        return Incident.objects.all()
    
class IncidentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PublicIncidentCreateView(generics.GenericAPIView):
    serializer_class = IncidentSerializer
    permission_classes = []

    def post(self, request):
            incident_description = request.data.get("incident")
            if not incident_description:
                return Response({"description": ["Поле 'incident' обязательно."]}, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "type": "incident",
                "topic": "Публичный отчет",
                "description": incident_description,
                "status": "new",
                "created_by": None,  # Устанавливаем значение для поля
                "team": "Клиенты",
            }

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)