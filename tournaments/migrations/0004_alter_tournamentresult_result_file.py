# Generated by Django 4.1.5 on 2023-06-05 12:25

import common.storage
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tournaments", "0003_alter_tournament_is_draft"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournamentresult",
            name="result_file",
            field=common.storage.RawFileField(upload_to="tournament_results/"),
        ),
    ]