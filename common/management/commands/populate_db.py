import datetime
import json

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from meetings.models import Meeting, RecurringMeeting, OneTimeMeeting
from tournaments.models import (
    Tournament,
    Registration,
    RegisteredPlayer,
    ScheduledActivity,
)


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        data = json.load(open("data/krakow.json", "r"))

        for recurring_meeting in data["recurring_meetings"]:
            recurring_meeting["start_time"] = datetime.time.fromisoformat(
                recurring_meeting["start_time"]
            )
            if recurring_meeting["end_time"]:
                recurring_meeting["end_time"] = datetime.time.fromisoformat(
                    recurring_meeting["end_time"]
                )
            RecurringMeeting.objects.create(**recurring_meeting)

        self.stdout.write("Meetings created.", ending="\n")

        for tournament in data["tournaments"]:
            registration = tournament.pop("registration")
            scheduled_activities = tournament.pop("scheduled_activities")
            registered_players = tournament.pop("registered_players")

            tournament = Tournament.objects.create(**tournament)

            Registration.objects.create(**registration, tournament=tournament)

            for scheduled_activity in scheduled_activities:
                ScheduledActivity.objects.create(
                    **scheduled_activity, tournament=tournament
                )

            for registered_player in registered_players:
                RegisteredPlayer.objects.create(
                    **registered_player, tournament=tournament
                )

        self.stdout.write("Tournaments created.", ending="\n")

        if not User.objects.filter(username="admin").exists():
            user = User.objects.create_user("admin", password="admin")
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write("Super user created.", ending="\n")
