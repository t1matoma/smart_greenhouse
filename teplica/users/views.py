from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegisterForm, GreenhouseForm
from .models import Greenhouse

def register(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        greenhouse_form = GreenhouseForm(request.POST)
        if user_form.is_valid() and greenhouse_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])  # Хешируем пароль
            user.save()
            
            # Привязываем теплицу к пользователю
            greenhouse = greenhouse_form.save(commit=False)
            greenhouse.user = user
            greenhouse.save()

            login(request, user)  # Авторизуем пользователя после регистрации
            return redirect("profile")
    else:
        user_form = UserRegisterForm()
        greenhouse_form = GreenhouseForm()

    return render(request, "users/register.html", {"user_form": user_form, "greenhouse_form": greenhouse_form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile")
    return render(request, "users/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user_greenhouses = Greenhouse.objects.filter(user=request.user)
    return render(request, "users/profile.html", {"greenhouses": user_greenhouses})
