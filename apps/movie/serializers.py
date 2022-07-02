from rest_framework import serializers
from .models import Movie, MovieImage
from apps.review.serializers import ReviewSerializer

from ..review.models import Review


class MovieImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            requests = self.context.get('requests')
            if requests is not None:
                url = requests.build_absolute_uri(url)
        else:
            url = ""
        return url


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def to_representation(self, instance):
        rep = super(MovieSerializer, self).to_representation(instance)
        rep['images'] = MovieImageSerializer(MovieImage.objects.filter(movie=instance.id), many=True).data
        rep['reviews'] = ReviewSerializer(instance.review.filter(product=instance.id), many=True).data
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) != 0:
            rep['tolal_rating'] = sum(total_rating)/len(total_rating)
        else:
            rep['total_rating'] = ""
        rep['comments'] = ReviewSerializer(Review.objects.filter(product_id=instance), many=True).data
        return  rep







