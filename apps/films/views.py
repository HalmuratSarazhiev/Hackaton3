from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Favorite
from .serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from ..review.permissions import IsReviewAuthor


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
# Create your views here.

    def get_permissions(self):
        if self.action in ['list', 'retrive']:
            permissions = []
        elif self.action == 'favorite':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsReviewAuthor]
        return [permission() for permission in permissions]
    # Add favorite
    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        review = self.get_object()
        favorite_obj, _ = Favorite.objects.get_or_create(review=review, user=request.user)
        favorite_obj.favorite = not favorite_obj.favorite
        favorite_obj.save()
        status = 'favorite'
        if not favorite_obj.favorite:
            status = 'Not favorite'
        return Response({'status': status})

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)
        return super().get_queryset()