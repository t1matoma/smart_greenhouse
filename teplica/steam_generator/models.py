from django.db import models
from users.models import Greenhouse  # Импортируем модель теплицы

class Evaporation(models.Model):
    STATUS_CHOICES = [
        ('on', 'Включено'),
        ('off', 'Выключено'),
    ]

    greenhouse = models.OneToOneField(Greenhouse, on_delete=models.CASCADE)  # Привязка к теплице
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='off')
    start_time = models.TimeField(null=True, blank=True)  
    duration = models.IntegerField(default=30)  

    def __str__(self):
        return f"Пароиспарение ({self.greenhouse.name}): {self.get_status_display()} | Начало: {self.start_time} | Длительность: {self.duration} мин."