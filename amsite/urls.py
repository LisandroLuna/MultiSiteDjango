"""Defines URL patterns for amsite."""
from django.urls import path
from . import views


app_name = 'amsite'

urlpatterns = [
    #Home page
    path('', views.amsite, name='amsite'),
    # Albums page
    path('albums/', views.albums, name='albums'),
    # Detail page for a single album
    path('albumdetail/<int:album_id>/', views.albumdetail, name='albumdetail'),
    # Adding new album
    path('newalbum/', views.newalbum, name='newalbum'),
    # Editing new album
    path('editalbum/<int:album_id>/', views.editalbum, name='editalbum'),
    # Adding new song
    path('newsong/<int:album_id>/', views.newsong, name='newsong'),
    # Editing new song
    path('editsong/<int:song_id>/', views.editsong, name='editsong'),
]

