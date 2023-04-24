from modeltranslation.translator import TranslationOptions, register

from tournaments.models import (
    Tournament,
    Registration,
    ScheduledActivity,
    TournamentResult,
)


@register(Tournament)
class TournamentTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
        "place",
        "additional_info",
        "address",
        "address_map_link",
        "prizes",
        "fee",
        "game_rules",
        "handicap_rules",
        "contact",
    )


@register(Registration)
class RegistrationTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(ScheduledActivity)
class ScheduledActivityTranslationOptions(TranslationOptions):
    fields = ("activity_name",)


@register(TournamentResult)
class TournamentResultTranslationOptions(TranslationOptions):
    fields = ("name",)
