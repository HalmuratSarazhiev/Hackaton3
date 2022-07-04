from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Movie, Favorite
from .serializers import MovieSerializer
from ..review.permissions import IsReviewAuthor



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    search_fields = ['title', 'year']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('year', 'title', 'category')



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
    def favorite(self, request, *args, **kwargs):
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