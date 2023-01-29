from rest_framework import routers

from sgfs.api.views import SgfViewSet

router = routers.SimpleRouter()

router.register("sgfs", SgfViewSet, basename="sgfs")

urlpatterns = router.urls
