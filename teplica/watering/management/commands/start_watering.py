from django.core.management.base import BaseCommand
from watering.models import WateringStatus

class Command(BaseCommand):
    help = 'Запускает полив'

    def handle(self, *args, **kwargs):
        watering_status = WateringStatus.objects.last()  # Берём последнюю запись

        if watering_status:
            if watering_status.status == 'started':
                self.stdout.write(self.style.WARNING('Полив уже начался'))
            else:
                watering_status.status = 'started'  # Обновляем статус
                watering_status.save()
                self.stdout.write(self.style.SUCCESS('Полив начался'))
        else:
            self.stdout.write(self.style.ERROR('Нет сохранённых данных о поливе. Сначала настройте полив.'))
