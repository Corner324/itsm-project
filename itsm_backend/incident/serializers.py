from rest_framework import serializers
from .models import Incident

class IncidentSerializer(serializers.ModelSerializer):
    created_by_username = serializers.ReadOnlyField(source='created_by.username')  # Имя пользователя, создавшего заявку

    class Meta:
        model = Incident
        fields = [
            'id',               # ID заявки
            'type',             # Тип заявки (например, "Инцидент", "Запрос")
            'topic',            # Тема заявки
            'description',      # Описание
            'status',           # Статус (например, "Новая", "В работе")
            'team',             # Ответственная команда
            'responsible',      # Ответственный сотрудник
            'created_at',       # Дата регистрации
            'updated_at',       # Дата последнего обновления
            'created_by_username',  # Имя пользователя, создавшего заявку
        ]
        read_only_fields = [
            'id',               # ID заявки нельзя изменять
            'created_at',       # Дата регистрации — только для чтения
            'updated_at',       # Дата обновления — только для чтения
            'created_by_username',  # Имя пользователя — только для чтения
        ]



class IncidentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['status']
