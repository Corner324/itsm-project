from django.conf import settings
from django.db import models

class Incident(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('resolved', 'Завершена'),
        ('rejected', 'Отклонена'),
    ]

    TYPE_CHOICES = [
        ('issue', 'Проблема'),
        ('request', 'Запрос'),
        ('incident', 'Инцидент'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='issue')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)  # Поле для даты создания
    updated_at = models.DateTimeField(auto_now=True)  # Поле для даты последнего обновления
    team = models.CharField(max_length=255, null=True, blank=True)
    responsible = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='incidents'
    )

    def __str__(self):
        return self.title


