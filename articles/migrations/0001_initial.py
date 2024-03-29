# Generated by Django 4.1.5 on 2023-04-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=100)),
                ("html_content", models.TextField()),
                ("is_draft", models.BooleanField(default=False)),
                ("author", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
