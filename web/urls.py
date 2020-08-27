"""Defines URL patterns for web."""
from django.conf.urls import url
from . import views

urlpatterns = [
    #Home page
    url('', views.index, name='index')
]

