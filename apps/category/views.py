
from .models import Category
from .serializers import CategorySerializers
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
# Create your views here.
