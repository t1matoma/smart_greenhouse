from django.shortcuts import render, redirect
from .models import WateringStatus
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def watering(request):
    watering_status, created = WateringStatus.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')  
        print(f"POST запрос пришел! Действие: {action}")

        if action == 'stop' and watering_status and watering_status.status == 'started':
            watering_status.status = 'stopped'
            watering_status.save()
            print("Полив остановлен через веб-интерфейс.")
            return redirect('watering')

        elif action == 'postpone' and watering_status:
            watering_status.postponed_time = timezone.now() + timezone.timedelta(hours=1)
            watering_status.save()
            print("Полив отложен на 1 час.")
            return redirect('watering')

        elif action == 'save_changes' and watering_status:
            new_watering_days = request.POST.get('watering_days')
            new_watering_time = request.POST.get('watering_time')
            new_duration = request.POST.get('duration')
            new_volume = request.POST.get('volume')

            print(f"Дни полива: {new_watering_days}")
            print(f"Время полива: {new_watering_time}")
            print(f"Длительность: {new_duration}")
            print(f"Объем: {new_volume}")

            if new_watering_days:
                watering_status.watering_days = new_watering_days
            if new_watering_time:
                watering_status.watering_time = timezone.datetime.strptime(new_watering_time, '%H:%M').time()
            if new_duration:
                watering_status.duration = int(new_duration)
            if new_volume:
                watering_status.volume = int(new_volume)

            watering_status.save()
            print("Данные успешно сохранены!")
            return redirect('watering')

    next_watering = watering_status.get_next_watering() if watering_status else None

    return render(request, "watering/watering.html", {
        "watering_status": watering_status,
        "next_watering": next_watering
    })