from django.db import models
from users.models import Greenhouse  # Импортируем модель теплицы

class LightingStatus(models.Model):
    STATUS_CHOICES = [
        ('on', 'Включено'),
        ('off', 'Выключено'),
    ]

    greenhouse = models.OneToOneField(Greenhouse, on_delete=models.CASCADE)  # Привязка к теплице
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='off')
    start_time = models.TimeField(null=True, blank=True) 
    end_time = models.TimeField(null=True, blank=True) 
    
    def __str__(self):
        return f"Освещение ({self.greenhouse.name}): {self.get_status_display()} (с {self.start_time} до {self.end_time})"