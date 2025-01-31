from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

class WateringStatus(models.Model):
    STATUS_CHOICES = [
        ('started', 'Начался полив'),
        ('stopped', 'Полив остановлен'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='stopped')
    duration = models.PositiveIntegerField(default=0)  # Длительность полива в минутах
    volume = models.PositiveIntegerField(default=0)  # Объем полива в литрах
    created_at = models.DateTimeField(auto_now_add=True)
    watering_time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязка к пользователю

    # Новые поля для хранения дней недели и времени полива
    watering_days = models.CharField(max_length=255, blank=True, null=True)  # Дни недели, например, "Понед, Среда, Пятница"
    postponed_time = models.DateTimeField(null=True, blank=True)  # Отложенное время полива

    def __str__(self):
        return f'{self.status} с {self.created_at}'

    def get_next_watering(self):
        # Логика для вычисления ближайшего полива
        if self.watering_days and self.watering_time:
            days = self.watering_days.split(', ')  # Разделяем дни
            current_day = timezone.now().weekday()  # Получаем текущий день недели
            current_time = timezone.now().time()  # Получаем текущее время

            watering_time = self.watering_time

            print(f"Дни полива: {days}")
            print(f"Текущее время: {current_time}")
            print(f"Текущий день: {current_day}")
            print(f"Время полива: {watering_time}")

            # Маппинг дней недели на числа (0 - понедельник, 6 - воскресенье)
            weekday = {
                "понед": 0, "вторник": 1, "среда": 2, "четверг": 3, 
                "пятница": 4, "суббота": 5, "воскресенье": 6
            }

            # Для каждого дня полива ищем ближайшее время
            next_watering_date = None
            for day in days:
                day = day.strip().lower()  # Приводим к нижнему регистру и убираем лишние пробелы
                watering_day = weekday.get(day)

                print(f"Обрабатываем день: {day}, код дня: {watering_day}")
                if watering_day is None:
                    continue

                # Если время полива уже прошло, выбираем следующий день
                if watering_day < current_day or (watering_day == current_day and watering_time <= current_time):
                    watering_day = (watering_day + 1) % 7

                # Вычисляем следующее время полива
                next_watering_date = timezone.now().replace(
                    hour=watering_time.hour, minute=watering_time.minute,
                    second=0, microsecond=0
                ) + timedelta(days=(watering_day - current_day) % 7)

                print(f"Следующий полив будет: {next_watering_date}")

                # Учитываем отложенное время
                if self.postponed_time:
                    next_watering_date = min(next_watering_date, self.postponed_time)
                    print(f"С учётом отложенного времени, полив будет: {next_watering_date}")

                break  # Останавливаем цикл, когда нашли первый ближайший полив

            return next_watering_date

        return None