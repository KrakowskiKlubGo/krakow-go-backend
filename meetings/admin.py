from django.contrib import admin
from model_clone import CloneModelAdmin

from common.admin import CloneTranslationModelAdmin
from meetings.models import MeetingParticipant, Meeting


class MeetingParticipantInlinie(admin.TabularInline):
    fk_name = "meeting"
    model = MeetingParticipant
    extra = 0


@admin.register(Meeting)
class MeetingAdmin(CloneTranslationModelAdmin):
    list_display = ("name_pl", "date", "start_time", "end_time")
    inlines = [MeetingParticipantInlinie]
