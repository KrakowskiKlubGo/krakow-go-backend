from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline

from common.admin import CloneTranslationModelAdmin
from tournaments.models import Registration, Tournament, RegisteredPlayer


class RegistrationInline(TranslationTabularInline):
    model = Registration


class RegisteredPlayerInline(admin.TabularInline):
    fk_name = "tournament"
    model = RegisteredPlayer
    readonly_fields = ("timestamp",)
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
    inlines = [RegistrationInline, RegisteredPlayerInline]
    fieldsets = (
        (
            "General",
            {
                "fields": (
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
