import datetime

import pytest
from rest_framework.reverse import reverse

from tournaments.const import PlayerRank
from tournaments.tests.factories import TournamentFactory, RegisteredPlayerFactory

pytestmark = pytest.mark.django_db


def test_api_correctly_returns_tournaments_list(api_client, tournament):
    newest_tournament = TournamentFactory(
        start_date=datetime.date.today() + datetime.timedelta(days=300),
        end_date=datetime.date.today() + datetime.timedelta(days=301),
    )
    response = api_client.get(
        reverse(
            "tournaments:tournaments-list",
        )
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["code"] == newest_tournament.code


@pytest.mark.parametrize(
    "language",
    [
        "pl",
        "en",
    ],
)
def test_api_correctly_returns_tournament_details_for_different_languages(
    api_client, tournament, language
):
    response = api_client.get(
        reverse(
            "tournaments:tournaments-detail",
            kwargs={"code": tournament.code},
        ),
        HTTP_ACCEPT_LANGUAGE=language,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["code"] == tournament.code
    assert data["name"] == getattr(tournament, f"name_{language}")
    assert data["image"] == None
    assert data["start_date"] == str(tournament.start_date)
    assert data["end_date"] == str(tournament.end_date)

    assert data["registration_info"]["end_date"] == str(
        tournament.registration.end_date
    )
    assert data["registration_info"]["description"] == getattr(
        tournament.registration, f"description_{language}"
    )
    assert data["registration_info"]["player_limit"] == None
    assert data["registration_info"]["email_required"] == False
    assert (
        data["registration_info"]["registered_players"]
        == tournament.registered_players.count()
    )

    assert data["tournament_info"]["is_draft"] == tournament.is_draft
    assert data["tournament_info"]["organizer"] == tournament.organizer
    assert data["tournament_info"]["referee"] == tournament.referee
    assert data["tournament_info"]["description"] == tournament.description
    assert data["tournament_info"]["additional_info"] == getattr(
        tournament, f"additional_info_{language}"
    )
    assert data["tournament_info"]["place"] == getattr(tournament, f"place_{language}")
    assert data["tournament_info"]["address"] == getattr(
        tournament, f"address_{language}"
    )
    assert data["tournament_info"]["address_map_link"] == getattr(
        tournament, f"address_map_link_{language}"
    )
    assert data["tournament_info"]["prizes"] == getattr(
        tournament, f"prizes_{language}"
    )
    assert data["tournament_info"]["fee"] == getattr(tournament, f"fee_{language}")
    assert data["tournament_info"]["game_rules"] == getattr(
        tournament, f"game_rules_{language}"
    )
    assert data["tournament_info"]["komi"] == tournament.komi
    assert data["tournament_info"]["rules_system"] == tournament.rules_system.label
    assert (
        data["tournament_info"]["tournament_class"] == tournament.tournament_class.label
    )
    assert data["tournament_info"]["rounds"] == tournament.rounds
    assert data["tournament_info"]["handicap_rules"] == getattr(
        tournament, f"handicap_rules_{language}"
    )
    assert data["tournament_info"]["time_control"] == tournament.time_control
    assert data["tournament_info"]["contact"] == getattr(
        tournament, f"contact_{language}"
    )

    assert (
        len(data["tournament_info"]["scheduled_activities"])
        == tournament.scheduled_activities.count()
    )
    for activity in tournament.scheduled_activities.all():
        assert {
            "activity_name": activity.activity_name,
            "date": str(activity.date),
            "time": activity.time.strftime("%H:%M"),
        } in data["tournament_info"]["scheduled_activities"]

    for result in tournament.tournament_results.all():
        assert result.id in data["tournament_results"]


def test_api_correctly_returns_registered_players(api_client, tournament):
    last_player = RegisteredPlayerFactory(
        tournament=tournament, rank=PlayerRank.EGF_1_DAN
    )

    response = api_client.get(
        reverse(
            "tournaments:tournaments-get-registered-players",
            kwargs={"code": tournament.code},
        )
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 11

    assert data[10]["first_name"] == last_player.first_name
    assert data[10]["last_name"] == last_player.last_name
    assert data[10]["rank"] == "1 dan"
    assert data[10]["city_club"] == last_player.city_club
    assert data[10]["country"] == last_player.country
    assert data[10]["is_paid"] == last_player.is_paid
    assert data[10]["egf_pid"] == str(last_player.egf_pid)


@pytest.mark.parametrize(
    "language",
    [
        "pl",
        "en",
    ],
)
def test_api_correctly_returns_tournament_results_for_different_languages(
    api_client,
    tournament,
    language,
):
    last_order_result = tournament.tournament_results.first()
    last_order_result.order = 999999
    last_order_result.save()
    response = api_client.get(
        reverse(
            "tournaments:tournaments-get-results",
            kwargs={"code": tournament.code},
        ),
        HTTP_ACCEPT_LANGUAGE=language,
    )
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 2
    assert data[0]["name"] == getattr(last_order_result, f"name_{language}")
    assert data[0]["type"] == "standings"
    assert (
        data[0]["timestamp"]
        == last_order_result.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f") + "Z"
    )


@pytest.mark.parametrize(
    ("language", "expected_message"),
    [
        ("pl", "Zostałeś zapisany na turniej. Do zobaczenia!"),
        ("en", "You have been registered for the tournament. See you there!"),
    ],
)
def test_api_correctly_register_player_and_return_on_register_list_response_message_for_different_languages(
    api_client, captcha_data, tournament, language, expected_message
):
    response = api_client.post(
        reverse(
            "tournaments:tournaments-register-player",
            kwargs={"code": tournament.code},
        ),
        data={
            "first_name": "Jan",
            "last_name": "Testowy",
            "city_club": "Warszawa",
            "country": "PL",
            "rank": PlayerRank.EGF_1_DAN.value,
            "phone": "123456789",
            "email": "test@gmail.com",
            "egf_pid": 123456789,
            **captcha_data,
        },
        format="json",
        HTTP_ACCEPT_LANGUAGE=language,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == expected_message


@pytest.mark.parametrize(
    ("language", "expected_message"),
    [
        ("pl", "Zostałeś dodany do listy oczekujących."),
        ("en", "You have been added to the waiting list."),
    ],
)
def test_api_correctly_register_player_and_return_on_waiting_list_response_message_for_different_languages(
    api_client, captcha_data, tournament, language, expected_message
):
    tournament.registration.player_limit = tournament.registered_players.count()
    tournament.registration.save()
    response = api_client.post(
        reverse(
            "tournaments:tournaments-register-player",
            kwargs={"code": tournament.code},
        ),
        data={
            "first_name": "Jan",
            "last_name": "Testowy",
            "city_club": "Warszawa",
            "country": "PL",
            "rank": PlayerRank.EGF_1_DAN.value,
            "phone": "123456789",
            "email": "test@gmail.com",
            "egf_pid": 123456789,
            **captcha_data,
        },
        format="json",
        HTTP_ACCEPT_LANGUAGE=language,
    )

    assert response.status_code == 201
    data = response.json()
    assert data["message"] == expected_message
