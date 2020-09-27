from django import forms
from .models import Album, Song


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'desc', 'img', 'year']
        labels = {'title': 'Título', 'desc': 'Descripcion', 'img': 'URL de Portada', 'year': 'Año (AAAA)'}
        widgets = {'desc': forms.Textarea(attrs={'cols': 80})}


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'title']
        labels = {'album': 'Album', 'title': 'Título'}


