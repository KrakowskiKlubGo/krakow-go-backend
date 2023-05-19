import pytest

from tournaments.tests.factories import (
    TournamentFactory,
    RegistrationFactory,
    RegisteredPlayerFactory,
    ScheduledActivityFactory,
    TournamentResultFactory,
)


@pytest.fixture
def tournament():
    tournament = TournamentFactory()
    RegistrationFactory(tournament=tournament)
    for _ in range(10):
        RegisteredPlayerFactory(tournament=tournament)
    for _ in range(3):
        ScheduledActivityFactory(tournament=tournament)

    for _ in range(2):
        TournamentResultFactory(tournament=tournament)
    yield tournament
