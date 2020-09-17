from django.shortcuts import render, redirect

from .forms import AlbumForm
from .models import Album


def amsite(request):
    """The home page for amsite"""
    return render(request, 'amsite/home.html')


def albums(request):
    """The albums page"""
    albums = Album.objects.order_by('year')
    context = {'albums': albums}
    return render(request, 'amsite/albums.html', context)


def albumdetail(request, album_id):
    """Show a single album"""
    album = Album.objects.get(id=album_id)
    songs = album.song_set.order_by('id')
    context = {'album': album, 'songs': songs}
    return render(request, 'amsite/albumdetail.html', context)

def newalbum(request):
    """Add new album."""
    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = AlbumForm()
    else:
    # POST data submitted; process data.
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('albums')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'amsite/newalbum.html', context)

