from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tournaments.api.serializers import (
    TournamentListSerializer,
    TournamentSerializer,
    CreateRegisteredPlayerSerializer,
    RegisteredPlayersSerializer,
    TournamentResultSerializer,
)
from tournaments.const import (
    PLAYER_ON_REGISTER_LIST_RESPONSE_MESSAGE,
    PLAYER_ON_WAITING_LIST_RESPONSE_MESSAGE,
)
from tournaments.models import Tournament, RegisteredPlayer, TournamentResult


class TournamentViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
    queryset = Tournament.objects.order_by("-start_date")
    lookup_field = "code"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["is_ended", "is_draft"]

    def get_serializer_class(self):
        if self.action == "list":
            return TournamentListSerializer
        elif self.action == "get_results":
            return TournamentResultSerializer
        elif self.action == "get_registered_players":
            return RegisteredPlayersSerializer
        return TournamentSerializer

    @action(detail=True, methods=["post"], url_path="register-player")
    def register_player(self, request, code):
        id = self.get_object().id
        serializer = CreateRegisteredPlayerSerializer(
            data={
                **request.data,
                "tournament_id": id,
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tournament = (
            Tournament.objects.select_related("registration")
            .prefetch_related("registered_players")
            .get(id=id)
        )
        if (
            tournament.registration.player_limit is not None
            and tournament.registered_players.count()
            > tournament.registration.player_limit
        ):
            message = PLAYER_ON_WAITING_LIST_RESPONSE_MESSAGE[request.LANGUAGE_CODE]
        else:
            message = PLAYER_ON_REGISTER_LIST_RESPONSE_MESSAGE[request.LANGUAGE_CODE]

        return Response(
            {
                "message": message,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(detail=True, methods=["get"], url_path="registered-players")
    def get_registered_players(self, request, code):
        serializer = self.get_serializer_class()(
            RegisteredPlayer.objects.filter(tournament__code=code)
            .all()
            .order_by("timestamp"),
            many=True,
        )
        return Response(serializer.data)

    @action(detail=True, methods=["get"], url_path="results")
    def get_results(self, request, code):
        serializer = self.get_serializer_class()(
            TournamentResult.objects.filter(tournament__code=code)
            .all()
            .order_by("-order"),
            many=True,
        )
        return Response(serializer.data)
