from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'desc', 'img', 'year']
        labels = {'title': 'Titulo', 'desc': 'Descripcion', 'img': 'URL de Portada', 'year': 'Año (AAAA)'}
        widgets = {'desc': forms.Textarea(attrs={'cols': 80})}
