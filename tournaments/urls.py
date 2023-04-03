from rest_framework import routers

from tournaments.api.views import TournamentViewSet

router = routers.SimpleRouter()
router.register(
    "tournaments",
    TournamentViewSet,
    basename="tournaments",
)

urlpatterns = router.urls
