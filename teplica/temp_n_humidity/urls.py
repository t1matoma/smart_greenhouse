from django.urls import path
from .views import temp_n_humidity
urlpatterns = [
    path('', temp_n_humidity, name='temp_n_humidity'),
]