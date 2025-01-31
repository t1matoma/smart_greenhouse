from django import forms
from django.contrib.auth.models import User
from .models import Greenhouse

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Поле пароля

    class Meta:
        model = User
        fields = ["username", "email", "password"]

class GreenhouseForm(forms.ModelForm):
    class Meta:
        model = Greenhouse
        fields = ["name"]
