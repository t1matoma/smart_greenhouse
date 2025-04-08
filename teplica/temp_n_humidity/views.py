from django.shortcuts import render, redirect
from .models import TempAndHumidity
from heating.models import HeatingStatus

def temp_n_humidity(request):
    heating_status = HeatingStatus.objects.first()
    max_temperature = heating_status.temperature if heating_status else 20  # Если отопление не задано, температура по умолчанию 20

    # Получаем или создаем настройки для текущего пользователя
    temp_and_humidity, created = TempAndHumidity.objects.get_or_create(user=request.user)

    if request.method == "POST":
        if 'save_temperature' in request.POST:
            temperature = request.POST.get("temperature")
            if temperature:
                temp_and_humidity.temperature = int(temperature)
                temp_and_humidity.save()

        if 'save_humidity' in request.POST:
            humidity = request.POST.get("humidity")
            if humidity:
                temp_and_humidity.humidity = int(humidity)
                temp_and_humidity.save()

        if 'toggle_temperature' in request.POST:
            temp_and_humidity.temperature_enabled = not temp_and_humidity.temperature_enabled
            temp_and_humidity.save()

        if 'toggle_humidity' in request.POST:
            temp_and_humidity.humidity_enabled = not temp_and_humidity.humidity_enabled
            temp_and_humidity.save()

        return redirect('temp_n_humidity')

    return render(request, "temp_n_hum/temp_n_hum.html", {
        "max_temperature": max_temperature,
        "temperature": temp_and_humidity.temperature,
        "humidity": temp_and_humidity.humidity,
        "temperature_enabled": temp_and_humidity.temperature_enabled,
        "humidity_enabled": temp_and_humidity.humidity_enabled
    })