import uuid

from django.db import models
from datetime import timedelta

from django.db.models import Q
from django.utils.timezone import now

from common.models import BaseModel
from meetings.const import DayOfWeek


class MeetingQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def upcoming(self):
        return self.filter(
            Q(
                onetimemeeting__isnull=False,
                onetimemeeting__date__gte=now().date(),
                onetimemeeting__date__lt=(now() + timedelta(days=14)).date(),
            )
            | Q(
                recurringmeeting__isnull=False,
            ),
            is_active=True,
        )


class Meeting(BaseModel):
    """
    Base model for meetings
    """

    code = models.CharField(
        max_length=36,
        unique=True,
        default=uuid.uuid4,
        help_text="Unique code visible in URL.",
    )
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=100)
    address_map_link = models.URLField(null=True, blank=True, max_length=400)
    is_active = models.BooleanField(default=True)

    objects = MeetingQuerySet.as_manager()

    @property
    def next_date(self):
        if hasattr(self, "onetimemeeting"):
            return self.onetimemeeting.date
        elif hasattr(self, "recurringmeeting"):
            return self.recurringmeeting.date
        else:
            return None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"


class OneTimeMeeting(Meeting):
    """
    Meeting that happens only once in a specific date.
    """

    date = models.DateField()

    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"


class RecurringMeeting(Meeting):
    """
    Meeting that happens regularly. Currently only weekly meetings on specific day
    of week are supported.
    """

    day_of_week = models.CharField(
        max_length=20,
        choices=DayOfWeek.choices,
    )

    @property
    def date(self):
        """
        Returns the closest date with proper day of week.
        """
        today = now().weekday()
        meeting_day = [day for day in DayOfWeek].index(self.day_of_week)
        days_until_meeting = (meeting_day - today) % 7
        next_meeting = now() + timedelta(days=days_until_meeting)

        return next_meeting.date()

    class Meta:
        verbose_name = "Spotkanie cykliczne"
        verbose_name_plural = "Spotkania cykliczne"
