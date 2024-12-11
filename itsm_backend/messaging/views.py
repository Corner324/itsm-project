from django.contrib.auth import get_user_model
from rest_framework import generics, permissions


from .models import Message
from .serializers import MessageSerializer
from django.db import models
from rest_framework.exceptions import ValidationError


class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Если передан параметр user, возвращает сообщения с конкретным пользователем.
        """
        user_id = self.request.query_params.get("user")
        CustomUser = get_user_model()
        if user_id:
            try:
                user = CustomUser.objects.get(id=user_id)
            except CustomUser.DoesNotExist:
                raise ValidationError({"detail": "Пользователь не найден."})
            return Message.objects.filter(
                models.Q(sender=self.request.user, receiver=user)
                | models.Q(sender=user, receiver=self.request.user)
            ).order_by("created_at")

        return Message.objects.filter(
            models.Q(sender=self.request.user) | models.Q(receiver=self.request.user)
        ).order_by("created_at")

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class MessageDetailView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
