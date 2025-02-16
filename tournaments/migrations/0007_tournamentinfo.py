# Generated by Django 4.1.5 on 2024-11-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tournaments", "0006_registration_email_required"),
    ]

    operations = [
        migrations.CreateModel(
            name="TournamentInfo",
            options={
                "verbose_name": "Turniej",
                "verbose_name_plural": "Turnieje",
            },
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
                ("name", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                (
                    "end_date",
                    models.DateField(
                        blank=True,
                        help_text="If tournament lasts one day then leave this field empty.",
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "registration_link",
                    models.URLField(blank=True, max_length=400, null=True),
                ),
                (
                    "results_link",
                    models.URLField(blank=True, max_length=400, null=True),
                ),
            ],
        ),
    ]
