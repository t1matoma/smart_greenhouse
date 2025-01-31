from django.urls import path
from .views import watering

urlpatterns = [
    path('', watering, name='watering'),
]