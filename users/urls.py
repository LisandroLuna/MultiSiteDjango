"""Defines URL patterns for users."""
from django.urls import path, include
from . import views


app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # Registro
    path('register/', views.register, name='register'),
]
