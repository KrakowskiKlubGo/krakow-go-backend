import datetime

import pytest
from rest_framework.reverse import reverse

from meetings.tests.factories import OneTimeMeetingFactory, RecurringMeetingFactory

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "language",
    [
        "en",
        "pl",
    ],
)
def test_api_correctly_get_meeting_list(api_client, language):
    incoming_one_time_meeting = OneTimeMeetingFactory(
        date=datetime.date.today() + datetime.timedelta(days=2),
    )
    recurring_meeting = RecurringMeetingFactory(
        day_of_week=datetime.date.today().strftime("%A"),
    )
    incoming_one_time_meeting_in_more_than_week = OneTimeMeetingFactory(  # noqa
        date=datetime.date.today() + datetime.timedelta(days=8),
    )
    past_one_time_meeting = OneTimeMeetingFactory(  # noqa
        date=datetime.date.today() - datetime.timedelta(days=1),
    )

    response = api_client.get(
        reverse(
            "meetings:meetings-list",
        ),
        HTTP_ACCEPT_LANGUAGE=language,
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

    assert data[0]["code"] == incoming_one_time_meeting.code
    assert data[0]["name"] == incoming_one_time_meeting.name
    assert data[0]["start_time"] == incoming_one_time_meeting.start_time.strftime(
        "%H:%M"
    )
    assert data[0]["end_time"] == incoming_one_time_meeting.end_time.strftime("%H:%M")
    assert data[0]["address"] == incoming_one_time_meeting.address

    assert data[1]["code"] == recurring_meeting.code
    assert data[1]["name"] == recurring_meeting.name
    assert data[1]["start_time"] == recurring_meeting.start_time.strftime("%H:%M")
    assert data[1]["end_time"] == recurring_meeting.end_time.strftime("%H:%M")
    assert data[1]["address"] == recurring_meeting.address


@pytest.mark.parametrize(
    "language",
    [
        "en",
        "pl",
    ],
)
def test_api_correctly_get_meeting_detail(api_client, language):
    incoming_one_time_meeting = OneTimeMeetingFactory(
        date=datetime.date.today() + datetime.timedelta(days=2),
    )
    response = api_client.get(
        reverse(
            "meetings:meetings-detail",
            kwargs={"code": incoming_one_time_meeting.code},
        ),
        HTTP_ACCEPT_LANGUAGE=language,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == incoming_one_time_meeting.name
    assert data["start_time"] == incoming_one_time_meeting.start_time.strftime("%H:%M")
    assert data["end_time"] == incoming_one_time_meeting.end_time.strftime("%H:%M")
    assert data["address"] == incoming_one_time_meeting.address
    assert data["address_map_link"] == incoming_one_time_meeting.address_map_link
    assert data["description"] == incoming_one_time_meeting.description
    assert data["date"] == incoming_one_time_meeting.date.strftime("%Y-%m-%d")
