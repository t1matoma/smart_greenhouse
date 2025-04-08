from django.core.management.base import BaseCommand
from watering.models import WateringStatus

class Command(BaseCommand):
    help = 'Останавливает полив'

    def handle(self, *args, **kwargs):
        watering_status = WateringStatus.objects.filter(status='started').last()

        if watering_status:
            watering_status.status = 'stopped'
            watering_status.save()
            self.stdout.write(self.style.SUCCESS('Полив остановлен'))
        else:
            self.stdout.write(self.style.WARNING('Полив не был начат или уже остановлен'))
