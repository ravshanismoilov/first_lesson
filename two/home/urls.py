from django.urls import path
from .views import get_age



urlpatterns = [
    path('', get_age, name='get_age'),
]