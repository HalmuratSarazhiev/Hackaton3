from rest_framework import serializers
from .models import Movie, MovieImage, Favorite
from apps.review.serializers import ReviewSerializer

from ..review.models import Review


class MovieImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieImage
        fields = '__all__'
    #
    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            requests = self.context.get('requests')
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url
    #
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep

 # def to_representation(self, instance):
 #        rep = super().to_representation(instance)
 #        rep['images'] = FilmImageSerializer(FilmImage.objects.filter(film=instance.id), many=True).data

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(MovieSerializer, self).to_representation(instance)
        rep['images'] = MovieImageSerializer(MovieImage.objects.filter(movie=instance.id), many=True).data
        rep['reviews'] = ReviewSerializer(instance.review.filter(movie=instance.id), many=True).data
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating)/len(total_rating)
        else:
            rep['total_rating'] = ""
        rep['reviews'] = ReviewSerializer(Review.objects.filter(movie_id=instance), many=True).data
        rep['favorite'] = instance.fav.filter(favorite=True).count()
        return  rep

#     3 add new code 17:56 2 july

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"





