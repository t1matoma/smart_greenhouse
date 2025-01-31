from django.contrib.auth.models import User
from django.db import models

class Greenhouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю
    name = models.CharField(max_length=100)  # Название теплицы
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f"{self.name} (Владелец: {self.user.username})"
