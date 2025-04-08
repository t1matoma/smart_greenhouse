from django.db import models
from users.models import Greenhouse  # Импортируем теплицу

class HeatingStatus(models.Model):
    STATUS_CHOICES = [
        ('on', 'Включено'),
        ('off', 'Выключено'),
    ]

    greenhouse = models.OneToOneField(Greenhouse, on_delete=models.CASCADE)  # Привязка к теплице
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='off') 
    temperature = models.IntegerField(default=20)

    def __str__(self):
        return f"Отопление ({self.greenhouse.name}): {self.get_status_display()} - {self.temperature}°C"