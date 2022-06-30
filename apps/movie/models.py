from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=80, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    year = models.IntegerField(verbose_name='Year')
    genre = models.CharField(max_length=80, verbose_name='Genre')

    def __str__(self):
        return self.title

class MovieImage(models.Model):
    image = models.ImageField(upload_to='images')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')