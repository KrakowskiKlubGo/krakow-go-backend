# Generated by Django 4.1.5 on 2023-05-12 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="code",
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
