from django.db.models import Count
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from meetings.api.serializers import (
    MeetingSerializer,
    MeetingParticipantCreateSerializer,
)
from meetings.models import Meeting


class MeetingViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all().annotate(
            participants_count=Count("participants", distinct=True),
        )


class MeetingParticipantCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = MeetingParticipantCreateSerializer
