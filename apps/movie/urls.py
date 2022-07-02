from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()

router.register('', MovieViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
