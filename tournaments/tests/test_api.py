import datetime

import pytest
from rest_framework.reverse import reverse

from tournaments.const import PlayerRank, PLAYER_ON_REGISTER_LIST_RESPONSE_MESSAGE
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
    "language",
    [
        "pl",
        "en",
    ],
)
def test_api_correctly_register_player_and_return_on_register_list_response_message_for_different_languages(
    api_client,
    captcha_data,
    tournament,
    language,
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
    assert data["message"] == PLAYER_ON_REGISTER_LIST_RESPONSE_MESSAGE[language]
