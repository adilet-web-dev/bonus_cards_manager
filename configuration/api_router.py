from rest_framework.routers import DefaultRouter
from apps.cards.api.viewsets import CardViewSet

router = DefaultRouter()
router.register("cards", CardViewSet)

urlpatterns = router.urls
