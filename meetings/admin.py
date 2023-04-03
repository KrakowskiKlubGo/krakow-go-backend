from django.contrib import admin
from model_clone import CloneModelAdmin

from meetings.models import MeetingParticipant, Meeting


class MeetingParticipantInlinie(admin.TabularInline):
    fk_name = "meeting"
    model = MeetingParticipant
    extra = 0


@admin.register(Meeting)
class MeetingAdmin(CloneModelAdmin):
    list_display = ("name", "date", "start_time", "end_time")
    inlines = [MeetingParticipantInlinie]
