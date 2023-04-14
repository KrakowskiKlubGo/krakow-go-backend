from django.contrib import admin

from common.admin import CloneTranslationModelAdmin
from meetings.models import (
    MeetingParticipant,
    Meeting,
    OneTimeMeeting,
    RecurringMeeting,
)


class MeetingParticipantInlinie(admin.TabularInline):
    fk_name = "meeting"
    model = MeetingParticipant
    extra = 0


@admin.register(OneTimeMeeting)
class MeetingAdmin(CloneTranslationModelAdmin):
    list_display = ("name_pl", "date", "start_time", "end_time")
    inlines = [MeetingParticipantInlinie]


@admin.register(RecurringMeeting)
class RecurringMeeting(CloneTranslationModelAdmin):
    list_display = ("name_pl", "day_of_week", "start_time", "end_time")
    inlines = [MeetingParticipantInlinie]
