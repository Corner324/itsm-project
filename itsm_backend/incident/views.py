from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Incident
from .serializers import IncidentSerializer, IncidentUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .models import Incident
from .serializers import IncidentSerializer

# Создание инцидента (только для сотрудников)
class IncidentCreateView(generics.CreateAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Получение инцидентов текущего пользователя
class MyIncidentsListView(generics.ListAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Incident.objects.filter(created_by=self.request.user)

# Получение всех инцидентов (для специалистов техподдержки)
class AllIncidentsListView(generics.ListAPIView):
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'support':
            raise PermissionError("У вас нет прав для просмотра всех заявок.")
        return Incident.objects.all()

# Обновление инцидента (только для специалистов техподдержки)
class IncidentUpdateView(generics.UpdateAPIView):
    serializer_class = IncidentUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role != 'support':
            raise PermissionError("Вы не можете обновлять заявки.")
        return Incident.objects.all()
    
class IncidentDetailView(generics.RetrieveAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]