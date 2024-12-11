from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("employee", "Сотрудник"),
        ("support", "Техподдержка"),
        ("admin", "Администратор"),
    ]
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default="employee")
