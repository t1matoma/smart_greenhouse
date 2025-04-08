from datetime import datetime
from django.shortcuts import render, redirect
from .models import Evaporation
from users.models import Greenhouse

def steam_generator(request):
    # Получаем теплицу текущего пользователя
    greenhouse = Greenhouse.objects.filter(user=request.user).first()

    if not greenhouse:
        return render(request, "steam_generator/steam_generator.html", {"error": "У вас нет теплицы."})

    
    evaporation_settings, _ = Evaporation.objects.get_or_create(greenhouse=greenhouse)

    if request.method == "POST":
        if "turn_on" in request.POST:
            evaporation_settings.status = "on"
        elif "turn_off" in request.POST:
            evaporation_settings.status = "off"
        elif "save_settings" in request.POST:
            start_time = request.POST.get("start_time")
            duration = request.POST.get("duration")

            if start_time:
                try:
                    evaporation_settings.start_time = datetime.strptime(start_time, "%H:%M").time()
                except ValueError:
                    pass  # Если вдруг формат неправильный, просто пропустим

            if duration:
                evaporation_settings.duration = int(duration)

        evaporation_settings.save()
        return redirect("steam_generator")

    return render(request, "steam_generator/steam_generator.html", {"evaporation_settings": evaporation_settings})