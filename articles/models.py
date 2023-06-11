import uuid

from django.db import models
from django.conf import settings


class Article(models.Model):
    """
    Article model represents a single HTML article in a specific language on the
    website.
    """

    code = models.CharField(max_length=36, default=uuid.uuid4)
    language = models.CharField(max_length=2, choices=settings.LANGUAGES)
    title = models.CharField(max_length=100)
    html_content = models.TextField()

    def __str__(self):
        return self.title + " (" + self.language + ")"

    class Meta:
        unique_together = ("code", "language")


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
