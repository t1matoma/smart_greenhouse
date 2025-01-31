from django.urls import path
from .views import ventilation
urlpatterns = [
    path('', ventilation, name='ventilation'),
]