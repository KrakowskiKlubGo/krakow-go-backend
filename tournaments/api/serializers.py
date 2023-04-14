from rest_framework import serializers

from tournaments.const import PlayerRank, RuleSystem
from tournaments.models import (
    Tournament,
    Registration,
    RegisteredPlayer,
    ScheduledActivity,
)


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

    rank = serializers.SerializerMethodField()

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


class ScheduledActivitySerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = ScheduledActivity
        fields = (
            "date",
            "time",
            "activity_name",
        )


class TournamentInfo(serializers.ModelSerializer):
    scheduled_activities = ScheduledActivitySerializer(many=True)
    rules_system = serializers.SerializerMethodField()

    class Meta:
        fields = (
            "is_draft",
            "is_ended",
            "organizer",
            "referee",
            "description",
            "additional_info",
            "place",
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
            "scheduled_activities",
            "contact",
        )
        model = Tournament

    def get_rules_system(self, obj):
        return RuleSystem(obj.rules_system).label


class TournamentSerializer(serializers.ModelSerializer):
    registration_info = RegistrationInfoSerializer(source="registration")
    registered_players = RegisteredPlayersSerializer(many=True)
    tournament_info = serializers.SerializerMethodField()

    class Meta:
        model = Tournament
        fields = (
            "name",
            "image",
            "start_date",
            "end_date",
            "registration_info",
            "registered_players",
            "tournament_info",
        )

    def get_tournament_info(self, obj):
        return TournamentInfo(obj).data
