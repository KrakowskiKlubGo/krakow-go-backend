from rest_framework import routers

from meetings.api.views import MeetingViewSet

router = routers.SimpleRouter()

router.register("meetings", MeetingViewSet, basename="meetings")

urlpatterns = router.urls
