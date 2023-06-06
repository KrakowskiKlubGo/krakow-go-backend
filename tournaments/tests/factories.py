import datetime

import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from tournaments.const import (
    TournamentClass,
    TournamentResultType,
    PlayerRank,
    RuleSystem,
)
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
    name_pl = factory.Sequence(lambda n: f"Turniej {n}")
    name_en = factory.Sequence(lambda n: f"Tournament {n}")
    start_date = datetime.date.today() + datetime.timedelta(days=7)
    end_date = datetime.date.today() + datetime.timedelta(days=8)
    place_pl = factory.Faker("word")
    place_en = factory.Faker("word")
    is_draft = False
    is_ended = False
    referee = factory.Faker("word")
    description_pl = factory.Faker("text")
    description_en = factory.Faker("text")
    additional_info_pl = factory.Faker("text")
    additional_info_en = factory.Faker("text")
    address_pl = factory.Faker("word")
    address_en = factory.Faker("word")
    address_map_link_pl = factory.Faker("url")
    address_map_link_en = factory.Faker("url")
    prizes_pl = factory.Faker("word")
    prizes_en = factory.Faker("word")
    fee_en = factory.Faker("word")
    fee_pl = factory.Faker("word")
    game_rules_pl = factory.Faker("word")
    game_rules_en = factory.Faker("word")
    komi = "6.5"
    rules_system = RuleSystem.MAC_MAHON
    tournament_class = TournamentClass.A
    rounds = 5
    handicap_rules_en = factory.Faker("word")
    handicap_rules_pl = factory.Faker("word")
    time_control = factory.Faker("word")
    contact_pl = factory.Faker("word")
    contact_en = factory.Faker("word")


class RegistrationFactory(DjangoModelFactory):
    class Meta:
        model = Registration

    end_date = datetime.date.today() + datetime.timedelta(days=7)
    description_en = factory.Faker("text")
    description_pl = factory.Faker("text")


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
    name_pl = factory.Sequence(lambda n: f"Wyniki-{n}")
    name_en = factory.Sequence(lambda n: f"Results-{n}")
    type = TournamentResultType.STANDINGS
    result_file = factory.django.FileField()
    order = factory.sequence(lambda n: n)

    class Meta:
        model = TournamentResult
