from django.contrib import admin

from common.admin import CloneTranslationModelAdmin
from meetings.models import (
    OneTimeMeeting,
    RecurringMeeting,
)


@admin.register(OneTimeMeeting)
class MeetingAdmin(CloneTranslationModelAdmin):
    list_display = ("name_pl", "date", "start_time", "end_time")


@admin.register(RecurringMeeting)
class RecurringMeeting(CloneTranslationModelAdmin):
    list_display = ("name_pl", "day_of_week", "start_time", "end_time")
