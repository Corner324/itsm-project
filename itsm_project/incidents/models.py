from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import Service

User = get_user_model()

class Incident(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Open'), ('resolved', 'Resolved')]
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='incidents')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidents')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
