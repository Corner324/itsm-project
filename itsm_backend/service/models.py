from django.db import models

class BusinessService(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активная'),
        ('inactive', 'Неактивная'),
    ]
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name


class TechnicalService(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активная'),
        ('inactive', 'Неактивная'),
    ]
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    configuration_items = models.TextField()  # Здесь вместо описания будут конфигурационные единицы
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name
