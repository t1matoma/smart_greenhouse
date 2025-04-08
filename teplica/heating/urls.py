from django.urls import path
from .views import heating
urlpatterns = [
    path('', heating, name='heating'),
]