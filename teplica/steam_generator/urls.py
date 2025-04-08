from django.urls import path
from .views import steam_generator
urlpatterns = [
    path('', steam_generator, name='steam_generator'),
]