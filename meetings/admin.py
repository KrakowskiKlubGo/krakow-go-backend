from django.contrib import admin

from meetings.models import MeetingParticipant, Meeting


class MeetingParticipantInlinie(admin.TabularInline):
    model = MeetingParticipant
    extra = 0


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "start_time", "end_time")
    inlines = [MeetingParticipantInlinie]
