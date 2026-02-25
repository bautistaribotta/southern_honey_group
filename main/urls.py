from django.urls import path
from main.views import login, inicio

urlpatterns = [
    path('', login),
    path('inicio/', inicio)
]