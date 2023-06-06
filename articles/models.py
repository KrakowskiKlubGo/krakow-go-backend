import uuid

from django.db import models
from django.conf import settings


class SubMenu(models.Model):
    """
    SubMenu model represents a single submenu for grouping articles in website
    navigation. Articles without submenu will be displayed in main menu.
    """

    menu_display_name = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES)

    def __str__(self):
        return self.menu_display_name + " (" + self.language + ")"


class Article(models.Model):
    """
    Article model represents a single HTML article in a specific language on the
    website.
    """

    code = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    menu_display_name = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES)
    html_content = models.TextField()
    is_menu_visible = models.BooleanField(default=False)
    sub_menu = models.ForeignKey(
        "articles.SubMenu",
        on_delete=models.CASCADE,
        related_name="articles",
        null=True,
        blank=True,
        help_text="If blank then article will be displayed in main menu.",
    )

    def __str__(self):
        return self.menu_display_name + " (" + self.language + ")"


class ArticleImage(models.Model):
    """
    Represents a single image in an article.
    """

    article = models.ForeignKey(
        "articles.Article",
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="articles/images/")
