from rest_framework import serializers

from tournaments.const import PlayerRank
from tournaments.models import Tournament, Registration, RegisteredPlayer


class TournamentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ("id", "name", "start_date", "end_date")


class RegistrationInfoSerializer(serializers.ModelSerializer):
    registered_players = serializers.SerializerMethodField()
    tournament_id = serializers.IntegerField(source="tournament.id")

    class Meta:
        model = Registration
        fields = ("end_date", "player_limit", "registered_players", "tournament_id")

    def get_registered_players(self, obj):
        return obj.tournament.registered_players.count()


class RegisteredPlayersSerializer(serializers.ModelSerializer):
    rank = serializers.SerializerMethodField()

    class Meta:
        model = RegisteredPlayer
        fields = (
            "first_name",
            "last_name",
            "timestamp",
            "rank",
            "city_club",
            "country",
            "is_paid",
            "egf_pid",
        )

    def get_rank(self, obj):
        return PlayerRank(obj.rank).label


class CreateRegisteredPlayerSerializer(serializers.ModelSerializer):
    tournament_id = serializers.PrimaryKeyRelatedField(
        queryset=Tournament.objects.all(), write_only=True, source="tournament"
    )

    class Meta:
        model = RegisteredPlayer
        fields = (
            "tournament_id",
            "first_name",
            "last_name",
            "rank",
            "city_club",
            "country",
            "email",
            "phone",
            "egf_pid",
        )

    def validate(self, attrs):
        tournament = attrs["tournament"]
        if tournament.is_ended:
            raise serializers.ValidationError("Registration is closed.")
        if tournament.is_draft:
            raise serializers.ValidationError("Registration is closed.")
        return attrs


class TournamentInfo(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = (
            "name",
            "image",
            "place",
            "start_date",
            "end_date",
            "is_draft",
            "is_ended",
            "organizer",
            "referee",
            "description",
            "additional_info",
            "address",
            "address_map_link",
            "prizes",
            "fee",
            "game_rules",
            "komi",
            "rules_system",
            "tournament_class",
            "rounds",
            "handicap_rules",
            "time_control",
        )


class TournamentSerializer(serializers.ModelSerializer):
    registration_info = RegistrationInfoSerializer(source="registration")
    registered_players = RegisteredPlayersSerializer(many=True)
    tournament_info = serializers.SerializerMethodField()

    class Meta:
        model = Tournament
        fields = (
            "registration_info",
            "registered_players",
            "tournament_info",
        )

    def get_tournament_info(self, obj):
        return TournamentInfo(obj).data
