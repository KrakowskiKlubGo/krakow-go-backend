from rest_framework import viewsets

from tournaments.models import Tournament
from tournaments.api.serializers import TournamentListSerializer, TournamentSerializer


class TournamentListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tournament.objects.filter(is_draft=False).order_by("start_date")

    def get_serializer_class(self):
        if self.action == "list":
            return TournamentListSerializer
        return TournamentSerializer
