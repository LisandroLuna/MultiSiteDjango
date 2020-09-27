"""Defines URL patterns for startsite."""
from django.urls import path
from . import views


app_name = 'startsite'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]

