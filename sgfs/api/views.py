from rest_framework import viewsets

from sgfs.api.serializers import SgfListSerializer, SgfSerializer
from sgfs.models import Sgf


class SgfViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sgf.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return SgfListSerializer
        return SgfSerializer
