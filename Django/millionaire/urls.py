# posts/urls.py
from django.urls import path
from .views import play, add_question, game

urlpatterns = [
    path('', game, name='game'),
    path('game/', play, name='millionaire'),
    path('questions/', add_question, name='add_question'),
]