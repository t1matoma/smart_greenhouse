from django.db import models
from django.contrib.auth.models import User

class Ventilation(models.Model):
    STATUS_CHOICES = [
        ('on', 'Включено'),
        ('off', 'Выключено'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='off') 

    def __str__(self):
        return f"Вентиляция пользователя {self.user.username}: {self.get_status_display()}"