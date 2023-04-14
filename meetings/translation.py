from modeltranslation.translator import TranslationOptions, register

from meetings.models import Meeting, OneTimeMeeting, RecurringMeeting


@register(Meeting)
class MeetingTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


@register(OneTimeMeeting)
class OneTimeMeetingTranslationOptions(TranslationOptions):
    pass


@register(RecurringMeeting)
class RecurringMeetingTranslationOptions(TranslationOptions):
    pass
