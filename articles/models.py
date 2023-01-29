from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    html_content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
