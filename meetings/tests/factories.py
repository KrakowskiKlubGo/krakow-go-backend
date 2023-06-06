import datetime

import factory
from factory.django import DjangoModelFactory

from meetings.models import Meeting, OneTimeMeeting, RecurringMeeting


class MeetingFactory(DjangoModelFactory):
    class Meta:
        model = Meeting

    code = factory.Sequence(lambda n: f"meeting-{n}")
    name_pl = factory.Faker("name")
    name_en = factory.Faker("name")
    description_pl = factory.Faker("text")
    description_en = factory.Faker("text")
    start_time = datetime.time(19, 0, 0)
    end_time = datetime.time(21, 0, 0)
    address = factory.Faker("address")
    address_map_link = factory.Faker("url")


class OneTimeMeetingFactory(MeetingFactory):
    class Meta:
        model = OneTimeMeeting

    date = factory.Faker("date")


class RecurringMeetingFactory(MeetingFactory):
    class Meta:
        model = RecurringMeeting

    day_of_week = factory.Faker("day_of_week")
