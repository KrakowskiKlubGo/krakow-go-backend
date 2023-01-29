from django.contrib import admin

from tournaments.models import Registration, Tournament, RegisteredPlayer


class RegistrationInline(admin.TabularInline):
    model = Registration


class RegisteredPlayerInline(admin.TabularInline):
    model = RegisteredPlayer
    readonly_fields = ("timestamp",)
    extra = 0


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
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
                    "place",
                    "start_date",
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
