from rest_framework import routers

from meetings.api.views import MeetingViewSet, MeetingParticipantCreateViewSet

router = routers.SimpleRouter()

router.register("meetings", MeetingViewSet, basename="meeting")
router.register(
    "meeting-participants",
    MeetingParticipantCreateViewSet,
    basename="meeting-participants",
)

urlpatterns = router.urls
