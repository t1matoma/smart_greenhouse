from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ventilation
from temp_n_humidity.models import TempAndHumidity 

@login_required
def ventilation(request):
    ventilation_status, created = Ventilation.objects.get_or_create(user=request.user)

    temp_and_humidity = TempAndHumidity.objects.filter(user=request.user).last()

    # Если данных о температуре и влажности нет, выводим значения по умолчанию
    if temp_and_humidity:
        temperature = temp_and_humidity.temperature
        humidity = temp_and_humidity.humidity
    else:
        temperature = "Нет данных"
        humidity = "Нет данных"

    if request.method == "POST":
        ventilation_status.status = "off" if ventilation_status.status == "on" else "on"
        ventilation_status.save()
        return redirect("ventilation")

    return render(request, "ventilation/ventilation.html", {
        "ventilation_status": ventilation_status,
        "temperature": temperature,
        "humidity": humidity,
    })