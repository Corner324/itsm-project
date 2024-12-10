from django.db import models

class Service(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активная'),
        ('inactive', 'Неактивная'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    dependencies = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name