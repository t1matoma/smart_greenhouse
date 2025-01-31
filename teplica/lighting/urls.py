from django.urls import path
from .views import lighting
urlpatterns = [
    path('', lighting, name='lighting'),
]