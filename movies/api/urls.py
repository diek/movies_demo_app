from rest_framework import routers
from .views import MovieViewSet

router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet)
urlpatterns = router.urls
