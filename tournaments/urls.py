from rest_framework import routers

from tournaments.api.views import TournamentListViewSet

router = routers.SimpleRouter()
router.register(
    "tournaments",
    TournamentListViewSet,
    basename="tournaments",
)

urlpatterns = router.urls
