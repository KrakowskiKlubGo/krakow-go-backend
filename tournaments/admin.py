from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline

from common.admin import CloneTranslationModelAdmin
from tournaments.models import (
    Registration,
    Tournament,
    RegisteredPlayer,
    ScheduledActivity,
    TournamentResult,
)


class RegistrationInline(TranslationTabularInline):
    model = Registration


class RegisteredPlayerInline(admin.TabularInline):
    fk_name = "tournament"
    model = RegisteredPlayer
    readonly_fields = ("timestamp",)
    extra = 0


class ScheduledActivityInline(TranslationTabularInline):
    fk_name = "tournament"
    model = ScheduledActivity
    extra = 0


class TournamentResultInline(TranslationTabularInline):
    fk_name = "tournament"
    model = TournamentResult
    extra = 0


@admin.register(Tournament)
class TournamentAdmin(CloneTranslationModelAdmin):
    list_display = (
        "name_pl",
        "start_date",
        "place",
        "is_draft",
        "is_ended",
    )
    inlines = [
        RegistrationInline,
        RegisteredPlayerInline,
        ScheduledActivityInline,
        TournamentResultInline,
    ]
    fieldsets = (
        (
            "General",
            {
                "fields": (
                    "name",
                    "is_draft",
                    "is_ended",
                    "image",
                    "description",
                    "start_date",
                    "end_date",
                    "organizer",
                    "referee",
                    "additional_info",
                    "place",
                    "address",
                    "address_map_link",
                    "prizes",
                    "fee",
                    "contact",
                )
            },
        ),
        (
            "Ruleset",
            {
                "fields": (
                    "game_rules",
                    "komi",
                    "rules_system",
                    "tournament_class",
                    "rounds",
                    "handicap_rules",
                    "time_control",
                ),
            },
        ),
    )
