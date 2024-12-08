import csv

from django.contrib import admin
from django.http import HttpResponse
from model_clone import CloneModelAdminMixin
from modeltranslation.admin import TranslationTabularInline

from common.admin import CloneTranslationModelAdmin
from tournaments.models import (
    Registration,
    RegisteredPlayer,
    ScheduledActivity,
    TournamentResult,
    TournamentInfo,
    Tournament,
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
    actions = ["export_registered_players_as_csv"]
    list_display = ("name_pl", "start_date", "place", "is_draft")
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
                    "code",
                    "name",
                    "is_draft",
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

    def export_registered_players_as_csv(self, request, queryset):
        field_names = [
            "first_name",
            "last_name",
            "rank",
            "city_club",
            "country",
            "email",
            "phone",
            "egf_pid",
            "timestamp",
            "tournament",
        ]

        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = "attachment; filename=tournament-registered-players-list.csv"
        writer = csv.writer(response)

        writer.writerow(field_names)
        for tournament in queryset:
            for player in tournament.registered_players.all().order_by("timestamp"):
                row = writer.writerow([getattr(player, field) for field in field_names])

        return response

    export_registered_players_as_csv.short_description = (
        "Export Registered Players as CSV"
    )


@admin.register(TournamentInfo)
class TournamentInfoAdmin(
    CloneModelAdminMixin,
    admin.ModelAdmin,
):
    list_display = ("name", "start_date", "end_date")
