import uuid

from django.db import migrations, models


def populate_article_code(apps, schema_editor):
    Article = apps.get_model("articles", "Article")
    for article in Article.objects.all():
        article.code = uuid.uuid4()
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="title",
            new_name="menu_title",
        ),
        migrations.RemoveField(
            model_name="article",
            name="author",
        ),
        migrations.AddField(
            model_name="article",
            name="code",
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name="article",
            name="language",
            field=models.CharField(default="pl", max_length=2),
            preserve_default=False,
        ),
        migrations.RunPython(populate_article_code, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="article",
            name="code",
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
