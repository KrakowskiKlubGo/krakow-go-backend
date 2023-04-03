from django.db import models

from common.models import BaseModel


class Meeting(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=100)
    address_map_link = models.URLField(null=True, blank=True, max_length=400)

    def __str__(self):
        return self.name


class MeetingParticipant(models.Model):
    meeting = models.ForeignKey(
        "meetings.Meeting",
        on_delete=models.CASCADE,
        related_name="participants",
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
