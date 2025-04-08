from django.contrib.auth.models import User
from django.db import models

class Greenhouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} (Владелец: {self.user.username})"