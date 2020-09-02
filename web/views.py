from django.shortcuts import render
from .models import Album


def index(request):
    """The home page for web"""
    return render(request, 'web/home.html')


def albums(request):
    """The albums page"""
    albums = Album.objects.order_by('year')
    context = {'albums': albums}
    return render(request, 'web/albums.html', context)


def albumdetail(request, album_id):
    """Show a single album"""
    album = Album.objects.get(id=album_id)
    songs = album.song_set.order_by('id')
    context = {'album': album, 'songs': songs}
    return render(request, 'web/albumdetail.html', context)

