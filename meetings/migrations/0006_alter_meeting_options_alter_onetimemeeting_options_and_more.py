# Generated by Django 4.1.5 on 2024-12-01 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0005_populate_meetings_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="meeting",
            options={"verbose_name": "Wydarzenie", "verbose_name_plural": "Wydarzenia"},
        ),
        migrations.AlterModelOptions(
            name="onetimemeeting",
            options={"verbose_name": "Wydarzenie", "verbose_name_plural": "Wydarzenia"},
        ),
        migrations.AlterModelOptions(
            name="recurringmeeting",
            options={
                "verbose_name": "Spotkanie cykliczne",
                "verbose_name_plural": "Spotkania cykliczne",
            },
        ),
    ]