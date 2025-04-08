from django.shortcuts import render, redirect
from .models import HeatingStatus
from users.models import Greenhouse

def heating(request):
    # Получаем теплицу текущего пользователя
    greenhouse = Greenhouse.objects.filter(user=request.user).first()
    
    if not greenhouse:
        return render(request, "heating/heating.html", {"error": "У вас нет теплицы."})

    # Получаем статус отопления этой теплицы
    heating_status, created = HeatingStatus.objects.get_or_create(greenhouse=greenhouse)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'toggle': 
            heating_status.status = 'off' if heating_status.status == 'on' else 'on'
        elif action == 'set_temp':  
            new_temp = request.POST.get('temperature')
            if new_temp:
                heating_status.temperature = int(new_temp)

        heating_status.save()
        return redirect('heating')

    return render(request, "heating/heating.html", {"heating_status": heating_status})