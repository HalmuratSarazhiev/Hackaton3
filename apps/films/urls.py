from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieImageViewSet



router = DefaultRouter()

router.register('main', MovieViewSet)
router.register('image', MovieImageViewSet, basename='movie_image')

urlpatterns = []
urlpatterns.extend(router.urls)

