# posts/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, calculatorPageView
from millionaire.views import game

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('calculator/', calculatorPageView, name='calculator'),
    path('millionaire/', game, name='game'),
]
