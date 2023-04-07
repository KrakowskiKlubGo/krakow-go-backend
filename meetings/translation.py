from modeltranslation.translator import TranslationOptions, register

from meetings.models import Meeting


@register(Meeting)
class MeetingTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )
