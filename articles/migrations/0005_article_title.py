# Generated by Django 4.1.5 on 2023-06-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0004_rename_is_draft_article_is_menu_visible_articleimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="title",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
