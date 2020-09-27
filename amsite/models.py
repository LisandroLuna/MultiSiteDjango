from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    """Arctic Monkey's album"""
    title = models.CharField(max_length=50, blank=False)
    desc = models.CharField(max_length=500, default=' ')
    img = models.CharField(max_length=100,
                           default='https://www.generationsforpeace.org/wp-content/uploads/2018/03/empty.jpg')
    year = models.CharField(max_length=5, default='0000')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Song(models.Model):
    """Arctics Monkeys's Song"""
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title
