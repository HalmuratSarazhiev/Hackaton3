from django.db import models
from django.contrib.auth import get_user_model

from apps.category.models import Category

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=80, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    year = models.IntegerField(verbose_name='Year')
    genre = models.ForeignKey(Category,on_delete=models.CASCADE, max_length=80, verbose_name='Genre')

    def __str__(self):
        return self.title

class MovieImage(models.Model):
    image = models.ImageField(upload_to='images')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')


# class Favorite(models.Model):
#     class Meta:
#         abstract = True
#
#     user = models.ForeignKey(User, verbose_name="Пользователь")
#
#     def __str__(self):
#         return self.user.username
#
#
#
# class FavoriteMovie(Favorite):
#     class Meta:
#         db_table = "favorite_movies"
#
#     obj = models.ForeignKey(Movie, verbose_name="Статья")