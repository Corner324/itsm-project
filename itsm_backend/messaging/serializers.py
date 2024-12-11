from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source="sender.username")
    receiver_username = serializers.ReadOnlyField(source="receiver.username")

    class Meta:
        model = Message
        fields = [
            "id",
            "sender",
            "receiver",
            "content",
            "created_at",
            "is_read",
            "sender_username",
            "receiver_username",
        ]
        read_only_fields = [
            "id",
            "sender",
            "created_at",
            "is_read",
            "sender_username",
            "receiver_username",
        ]
