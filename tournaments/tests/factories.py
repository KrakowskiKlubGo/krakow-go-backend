import datetime

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from tournaments.const import TournamentClass, TournamentResultType, PlayerRank
from tournaments.models import (
    Tournament,
    Registration,
    RegisteredPlayer,
    ScheduledActivity,
    TournamentResult,
)


class TournamentFactory(DjangoModelFactory):
    class Meta:
        model = Tournament

    code = factory.Sequence(lambda n: f"tournament-{n}")
    name = factory.Sequence(lambda n: f"Tournament {n}")
    start_date = datetime.date.today() + datetime.timedelta(days=7)
    end_date = datetime.date.today() + datetime.timedelta(days=8)
    place = factory.Faker("word")
    is_draft = False
    is_ended = False
    referee = factory.Faker("word")
    description = factory.Faker("text")
    additional_info = factory.Faker("text")
    contact = factory.Faker("word")
    address = factory.Faker("word")
    address_map_link = factory.Faker("url")
    prizes = factory.Faker("word")
    fee = factory.Faker("word")
    game_rules = factory.Faker("word")
    komi = "6.5"
    rules_system = factory.Faker("word")
    tournament_class = TournamentClass.A
    rounds = 5
    handicap_rules = factory.Faker("word")
    time_control = factory.Faker("word")


class RegistrationFactory(DjangoModelFactory):
    class Meta:
        model = Registration

    end_date = datetime.date.today() + datetime.timedelta(days=7)
    description = factory.Faker("text")


class RegisteredPlayerFactory(DjangoModelFactory):
    class Meta:
        model = RegisteredPlayer

    first_name = factory.Faker("word")
    last_name = factory.Faker("word")
    rank = FuzzyChoice([x[0] for x in PlayerRank.choices])
    city_club = factory.Faker("city")
    country = factory.Faker("word")
    email = factory.Faker("email")
    phone = factory.Faker("word")
    egf_pid = factory.sequence(lambda n: n + 100000)


class ScheduledActivityFactory(DjangoModelFactory):
    class Meta:
        model = ScheduledActivity

    activity_name = factory.Faker("word")
    date = datetime.date.today() + datetime.timedelta(days=7)
    time = datetime.time(10, 0)


class TournamentResultFactory(DjangoModelFactory):
    name_pl = factory.Sequence(lambda n: f"Results-{n} PL")
    name_en = factory.Sequence(lambda n: f"Results-{n} EN")
    type = TournamentResultType.STANDINGS
    result_file = factory.django.FileField()
    order = factory.sequence(lambda n: n)

    class Meta:
        model = TournamentResult
