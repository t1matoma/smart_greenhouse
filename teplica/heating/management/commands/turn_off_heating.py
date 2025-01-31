from django.core.management.base import BaseCommand
from heating.models import HeatingStatus

class Command(BaseCommand):
    help = 'Выключает отопление'

    def handle(self, *args, **kwargs):
        heating, created = HeatingStatus.objects.get_or_create(id=1)
        heating.status = 'off'
        heating.save()
        self.stdout.write(self.style.SUCCESS('Отопление выключено'))
