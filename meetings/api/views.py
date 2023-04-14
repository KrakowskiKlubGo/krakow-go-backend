from datetime import timedelta

from django.db.models import Count, Q
from django.utils.timezone import now
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from meetings.api.serializers import (
    MeetingSerializer,
    MeetingParticipantCreateSerializer,
    MeetingListSerializer,
)
from meetings.models import Meeting


class MeetingViewSet(ReadOnlyModelViewSet):
    serializer_class = MeetingListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MeetingListSerializer
        return MeetingSerializer

    def get_queryset(self):
        queryset = Meeting.objects.all().annotate(
            participants_count=Count("participants", distinct=True),
        )
        if self.action == "list":
            queryset = queryset.filter(
                Q(
                    onetimemeeting__isnull=False,
                    onetimemeeting__date__gte=now().date(),
                    onetimemeeting__date__lt=(now() + timedelta(days=7)).date(),
                )
                | Q(
                    recurringmeeting__isnull=False,
                )
            )

        return queryset


class MeetingParticipantCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = MeetingParticipantCreateSerializer
