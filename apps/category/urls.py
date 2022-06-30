from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()

router.register('', CategoryViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
