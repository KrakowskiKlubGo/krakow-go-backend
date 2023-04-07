from modeltranslation.translator import TranslationOptions, register

from tournaments.models import Tournament, Registration


@register(Tournament)
class TournamentTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
        "additional_info",
        "address",
        "address_map_link",
        "prizes",
        "fee",
        "game_rules",
        "handicap_rules",
    )


@register(Registration)
class RegistrationTranslationOptions(TranslationOptions):
    fields = ("description",)
