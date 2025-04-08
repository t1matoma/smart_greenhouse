from django.core.management.base import BaseCommand
from lighting.models import LightingStatus

class Command(BaseCommand):
    help = "Включает освещение"

    def handle(self, *args, **kwargs):
        lighting_status, created = LightingStatus.objects.get_or_create(id=1)
        lighting_status.status = 'on'
        lighting_status.save()
        self.stdout.write(self.style.SUCCESS("Освещение включено"))
