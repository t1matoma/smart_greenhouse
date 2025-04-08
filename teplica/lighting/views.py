from django.shortcuts import render, redirect
from .models import LightingStatus
from users.models import Greenhouse
from django.utils import timezone

def lighting(request):
    # Получаем теплицу текущего пользователя
    greenhouse = Greenhouse.objects.filter(user=request.user).first()
    
    if not greenhouse:
        return render(request, "lighting/lighting.html", {"error": "У вас нет теплицы."})

    lighting_status, _ = LightingStatus.objects.get_or_create(greenhouse=greenhouse)

    if request.method == "POST":
        if "turn_on" in request.POST:
            lighting_status.status = "on"
        elif "turn_off" in request.POST:
            lighting_status.status = "off"
        elif "save_settings" in request.POST:
            start_time = request.POST.get("start_time")
            end_time = request.POST.get("end_time")
            if start_time:
                lighting_status.start_time = timezone.datetime.strptime(start_time, "%H:%M").time()
            if end_time:
                lighting_status.end_time = timezone.datetime.strptime(end_time, "%H:%M").time()

        lighting_status.save()
        return redirect("lighting")

    return render(request, "lighting/lighting.html", {"lighting_status": lighting_status})