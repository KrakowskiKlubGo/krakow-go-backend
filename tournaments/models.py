import uuid

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.db import models

from common.models import BaseModel
from tournaments.const import (
    RuleSystem,
    TournamentClass,
    PlayerRank,
    TournamentResultType,
)


class Tournament(BaseModel):
    code = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=100)
    is_draft = models.BooleanField(default=True)
    is_ended = models.BooleanField(default=False)
    organizer = models.TextField()
    referee = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(
        null=True,
        blank=True,
    )
    additional_info = models.TextField(
        null=True,
        blank=True,
    )
    contact = models.TextField(
        null=True,
        blank=True,
    )
    address = models.TextField(
        null=True,
        blank=True,
    )
    address_map_link = models.URLField(
        null=True,
        blank=True,
        max_length=400,
    )
    prizes = models.TextField(
        null=True,
        blank=True,
    )
    fee = models.TextField(
        null=True,
        blank=True,
    )
    prepaid_option = models.BooleanField(default=False)

    # ruleset
    game_rules = models.TextField(
        null=True,
        blank=True,
    )
    komi = models.CharField(
        max_length=5,
        null=True,
        blank=True,
    )
    rules_system = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=RuleSystem.choices,
    )
    tournament_class = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=TournamentClass.choices,
    )
    rounds = models.IntegerField(null=True, blank=True)
    handicap_rules = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    time_control = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    _clone_m2o_or_o2m_fields = [
        "scheduled_activities",
    ]

    def __str__(self):
        return self.name


class Registration(models.Model):
    tournament = models.OneToOneField(
        "tournaments.Tournament",
        on_delete=models.CASCADE,
    )
    end_date = models.DateField(null=True, blank=True)
    player_limit = models.IntegerField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.tournament.name} - Registration"

    class Meta:
        verbose_name = "Registration Info"
        verbose_name_plural = "Registration Info"


class RegisteredPlayer(models.Model):
    tournament = models.ForeignKey(
        "tournaments.Tournament",
        on_delete=models.CASCADE,
        related_name="registered_players",
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200, verbose_name="First name")
    last_name = models.CharField(max_length=200, verbose_name="Last name")
    rank = models.CharField(max_length=10, choices=PlayerRank.choices)
    city_club = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    is_paid = models.BooleanField(default=False)
    egf_pid = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )


class ScheduledActivity(models.Model):
    tournament = models.ForeignKey(
        "tournaments.Tournament",
        on_delete=models.CASCADE,
        related_name="scheduled_activities",
    )
    date = models.DateField()
    time = models.TimeField()
    activity_name = models.CharField(max_length=400)

    class Meta:
        verbose_name = "Scheduled Activity"
        verbose_name_plural = "Scheduled Activities"

    def __str__(self):
        return self.activity_name


class TournamentResult(models.Model):
    tournament = models.ForeignKey(
        "tournaments.Tournament",
        on_delete=models.CASCADE,
        related_name="tournament_results",
    )
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TournamentResultType.choices)
    result_file = models.FileField(
        upload_to="tournament_results/", storage=RawMediaCloudinaryStorage()
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tournament Result"
        verbose_name_plural = "Tournament Results"

    def __str__(self):
        return self.name
