from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    created_by_username = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Incident
        fields = [
            "id",
            "type",
            "topic",
            "description",
            "status",
            "team",
            "responsible",
            "created_at",
            "updated_at",
            "created_by_username",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "created_by_username",
        ]


class IncidentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ["status"]
