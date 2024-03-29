# Generated by Django 4.1.5 on 2023-04-28 09:51

from django.db import migrations, models
import django.db.models.deletion
import model_clone.mixin
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tournament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(default=uuid.uuid4, max_length=36, unique=True),
                ),
                ("name", models.CharField(max_length=100)),
                ("name_pl", models.CharField(max_length=100, null=True)),
                ("name_en", models.CharField(max_length=100, null=True)),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("place", models.CharField(max_length=100)),
                ("place_pl", models.CharField(max_length=100, null=True)),
                ("place_en", models.CharField(max_length=100, null=True)),
                ("is_draft", models.BooleanField(default=True)),
                ("is_ended", models.BooleanField(default=False)),
                ("organizer", models.TextField()),
                ("referee", models.CharField(blank=True, max_length=200, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("description_pl", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                ("additional_info", models.TextField(blank=True, null=True)),
                ("additional_info_pl", models.TextField(blank=True, null=True)),
                ("additional_info_en", models.TextField(blank=True, null=True)),
                ("contact", models.TextField(blank=True, null=True)),
                ("contact_pl", models.TextField(blank=True, null=True)),
                ("contact_en", models.TextField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("address_pl", models.TextField(blank=True, null=True)),
                ("address_en", models.TextField(blank=True, null=True)),
                (
                    "address_map_link",
                    models.URLField(blank=True, max_length=400, null=True),
                ),
                (
                    "address_map_link_pl",
                    models.URLField(blank=True, max_length=400, null=True),
                ),
                (
                    "address_map_link_en",
                    models.URLField(blank=True, max_length=400, null=True),
                ),
                ("prizes", models.TextField(blank=True, null=True)),
                ("prizes_pl", models.TextField(blank=True, null=True)),
                ("prizes_en", models.TextField(blank=True, null=True)),
                ("fee", models.TextField(blank=True, null=True)),
                ("fee_pl", models.TextField(blank=True, null=True)),
                ("fee_en", models.TextField(blank=True, null=True)),
                ("prepaid_option", models.BooleanField(default=False)),
                ("game_rules", models.TextField(blank=True, null=True)),
                ("game_rules_pl", models.TextField(blank=True, null=True)),
                ("game_rules_en", models.TextField(blank=True, null=True)),
                ("komi", models.CharField(blank=True, max_length=5, null=True)),
                (
                    "rules_system",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("mac_mahon", "MacMahon"),
                            ("swiss", "Swiss"),
                            ("round_robin", "Round Robin"),
                            ("swiss_round_robin", "Swiss Round Robin"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "tournament_class",
                    models.CharField(
                        blank=True,
                        choices=[("A", "A"), ("B", "B"), ("C", "C"), ("D", "D")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("rounds", models.IntegerField(blank=True, null=True)),
                (
                    "handicap_rules",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "handicap_rules_pl",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "handicap_rules_en",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "time_control",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(model_clone.mixin.CloneMixin, models.Model),
        ),
        migrations.CreateModel(
            name="TournamentResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("name_pl", models.CharField(max_length=200, null=True)),
                ("name_en", models.CharField(max_length=200, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("games_list", "Games list"),
                            ("players_list", "Players list"),
                            ("standings", "Standings"),
                        ],
                        max_length=20,
                    ),
                ),
                ("result_file", models.FileField(upload_to="tournament_results/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tournament_results",
                        to="tournaments.tournament",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tournament Result",
                "verbose_name_plural": "Tournament Results",
            },
        ),
        migrations.CreateModel(
            name="ScheduledActivity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("activity_name", models.CharField(max_length=400)),
                ("activity_name_pl", models.CharField(max_length=400, null=True)),
                ("activity_name_en", models.CharField(max_length=400, null=True)),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scheduled_activities",
                        to="tournaments.tournament",
                    ),
                ),
            ],
            options={
                "verbose_name": "Scheduled Activity",
                "verbose_name_plural": "Scheduled Activities",
            },
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("end_date", models.DateField(blank=True, null=True)),
                ("player_limit", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("description_pl", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                (
                    "tournament",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tournaments.tournament",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registration Info",
                "verbose_name_plural": "Registration Info",
            },
        ),
        migrations.CreateModel(
            name="RegisteredPlayer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "first_name",
                    models.CharField(max_length=200, verbose_name="First name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=200, verbose_name="Last name"),
                ),
                (
                    "rank",
                    models.CharField(
                        choices=[
                            ("5p", "5 pro"),
                            ("4p", "4 pro"),
                            ("3p", "3 pro"),
                            ("2p", "2 pro"),
                            ("1p", "1 pro"),
                            ("9d", "9 dan"),
                            ("8d", "8 dan"),
                            ("7d", "7 dan"),
                            ("6d", "6 dan"),
                            ("5d", "5 dan"),
                            ("4d", "4 dan"),
                            ("3d", "3 dan"),
                            ("2d", "2 dan"),
                            ("1d", "1 dan"),
                            ("1k", "1 kyu"),
                            ("2k", "2 kyu"),
                            ("3k", "3 kyu"),
                            ("4k", "4 kyu"),
                            ("5k", "5 kyu"),
                            ("6k", "6 kyu"),
                            ("7k", "7 kyu"),
                            ("8k", "8 kyu"),
                            ("9k", "9 kyu"),
                            ("10k", "10 kyu"),
                            ("11k", "11 kyu"),
                            ("12k", "12 kyu"),
                            ("13k", "13 kyu"),
                            ("14k", "14 kyu"),
                            ("15k", "15 kyu"),
                            ("16k", "16 kyu"),
                            ("17k", "17 kyu"),
                            ("18k", "18 kyu"),
                            ("19k", "19 kyu"),
                            ("20k", "20 kyu"),
                            ("21k", "21 kyu"),
                            ("22k", "22 kyu"),
                            ("23k", "23 kyu"),
                            ("24k", "24 kyu"),
                            ("25k", "25 kyu"),
                            ("26k", "26 kyu"),
                            ("27k", "27 kyu"),
                            ("28k", "28 kyu"),
                            ("29k", "29 kyu"),
                            ("30k", "30 kyu"),
                        ],
                        max_length=10,
                    ),
                ),
                ("city_club", models.CharField(max_length=200)),
                ("country", models.CharField(blank=True, max_length=200, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                ("is_paid", models.BooleanField(default=False)),
                ("egf_pid", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "tournament",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registered_players",
                        to="tournaments.tournament",
                    ),
                ),
            ],
        ),
    ]
