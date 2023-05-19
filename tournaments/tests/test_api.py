import pytest

pytestmark = pytest.mark.django_db


def test_api_get_tournament_list(client, tournament):
    response = client.get("/api/tournaments/")
    assert response.status_code == 200
