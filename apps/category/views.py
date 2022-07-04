

from .models import Category
from .serializers import CategorySerializers
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination

from ..films.models import Movie
from ..films.serializers import MovieSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = PageNumberPagination

    def get_serializer_context(self):
        return {"request": self.request}


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# Create your views here.
