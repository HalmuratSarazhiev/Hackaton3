from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

from apps.movie.models import User, Movie


class Review(models.Model):
    user = models.ForeignKey(User, related_name='review', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Movie, related_name='review', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return str(self.product.title)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='like')
    like = models.BooleanField(default=False)

    def __str__(self):
        return str(self.like)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorite')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.like)
