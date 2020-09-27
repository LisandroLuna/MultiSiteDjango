from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import AlbumForm, SongForm
from .models import Album, Song


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
    return render(request, 'amsite/album_detail.html', context)


@login_required
def newalbum(request):
    """Add new album."""
    if request.method != 'POST':
    # No data submitted; create a blank form.
        form = AlbumForm()
    else:
    # POST data submitted; process data.
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.owner = request.user
            new_album.save()
            return redirect('albums')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'amsite/new_album.html', context)

@login_required
def editalbum(request, album_id):
    """Edit album."""
    album = Album.objects.get(id=album_id)
    if album.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(instance=album, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('albumdetail', album_id=album_id)
    # Display a blank or invalid form
    context = {'album': album, 'form': form}
    return render(request, 'amsite/edit_album.html', context)


@login_required
def newsong(request, album_id):
    """Add new song"""
    album = Album.objects.get(id=album_id)
    if album.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data = blank form
        form = SongForm()
    else:
        # POST data is processed
        form = SongForm(data=request.POST)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.album = album
            new_song.owner = request.user
            new_song.save()
            return redirect('albumdetail', album_id=album_id)

    # Blank or invalid form
    context = {'album': album, 'form': form}
    return render(request, 'amsite/new_song.html', context)


@login_required
def editsong(request, song_id):
    """Edit existing song"""
    song = Song.objects.get(id=song_id)
    album = song.album
    if album.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = SongForm(instance=song)
    else:
        form = SongForm(instance=song, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('albumdetail', album_id=album.id)

    context = {'song': song, 'album': album, 'form': form}
    return render(request, 'amsite/edit_song.html', context)




