from rest_framework.viewsets import ReadOnlyModelViewSet

from meetings.api.serializers import (
    MeetingSerializer,
    MeetingListSerializer,
)
from meetings.models import Meeting


class MeetingViewSet(ReadOnlyModelViewSet):
    serializer_class = MeetingListSerializer
    lookup_field = "code"

    def get_serializer_class(self):
        if self.action == "list":
            return MeetingListSerializer
        return MeetingSerializer

    def get_queryset(self):
        queryset = Meeting.objects.filter(is_active=True)
        if self.action == "list":
            queryset = queryset.upcoming()
        return queryset
