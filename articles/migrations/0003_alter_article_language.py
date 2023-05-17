from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_rename_title_article_menu_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="language",
            field=models.CharField(
                choices=[("pl", "Polish"), ("en", "English")], max_length=2
            ),
        ),
        migrations.CreateModel(
            name="SubMenu",
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
                ("menu_display_name", models.CharField(max_length=100)),
                (
                    "language",
                    models.CharField(
                        choices=[("pl", "Polish"), ("en", "English")], max_length=2
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="article",
            old_name="menu_title",
            new_name="menu_display_name",
        ),
        migrations.AddField(
            model_name="article",
            name="sub_menu",
            field=models.ForeignKey(
                help_text="If blank then article will be displayed in main menu.",
                blank=True,
                null=True,
                on_delete=models.deletion.CASCADE,
                related_name="articles",
                to="articles.submenu",
            ),
        ),
    ]
