from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer
from django.db import models

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Показываем только сообщения, относящиеся к текущему пользователю
        return Message.objects.filter(
            models.Q(sender=self.request.user) | models.Q(receiver=self.request.user)
        ).order_by('created_at')

    def perform_create(self, serializer):
        # Автоматически устанавливаем отправителя как текущего пользователя
        serializer.save(sender=self.request.user)


class MessageDetailView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
