from django.db import models
from django.contrib.auth import get_user_model

from apps.category.models import Category

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=80, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    year = models.IntegerField(verbose_name='Year')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, max_length=80, verbose_name='Category')

    def __str__(self):
        return self.title

class MovieImage(models.Model):
    image = models.ImageField(upload_to='images')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')
# add favorite
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fav')
    review = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='fav')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.favorite)