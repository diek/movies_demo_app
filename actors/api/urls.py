from rest_framework import routers
from .views import ActorViewSet

router = routers.SimpleRouter()
router.register(r'actors', ActorViewSet)
urlpatterns = router.urls
