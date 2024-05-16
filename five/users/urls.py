from django.urls import path
from .views import Bookname


urlpatterns = [
    path('', Bookname, name='homepage'),
]