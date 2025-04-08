from django.db import models
from django.contrib.auth.models import User

class TempAndHumidity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю
    temperature = models.IntegerField(default=20)  # Температура в градусах Цельсия
    humidity = models.IntegerField(default=60)     # Влажность в процентах
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления
    temperature_enabled = models.BooleanField(default=True)
    humidity_enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Температура: {self.temperature}°C, Влажность: {self.humidity}%"

    class Meta:
        verbose_name = "Температура и влажность"
        verbose_name_plural = "Температуры и влажности"
