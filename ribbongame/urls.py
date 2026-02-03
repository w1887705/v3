from django.urls import path
from . import views

urlpatterns = [
    path('', views.ribbon_game, name='ribbon_game'),
]
