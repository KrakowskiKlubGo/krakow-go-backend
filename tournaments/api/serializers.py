from rest_framework import serializers

from tournaments.models import Tournament, Registration, RegisteredPlayer


class TournamentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ("id", "name", "start_date", "end_date")


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = (
            "end_date",
            "player_limit",
        )


class RegisteredPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredPlayer
        fields = (
            "name",
            "timestamp",
            "rank",
            "city_club",
            "country",
            "is_paid",
            "egf_pid",
        )


class TournamentSerializer(serializers.ModelSerializer):
    registration = RegistrationSerializer()
    registered_players = RegisteredPlayersSerializer(many=True)

    class Meta:
        model = Tournament
        fields = (
            "registration",
            "registered_players",
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
