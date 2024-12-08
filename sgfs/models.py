from django.db import models

from sgfs.const import SGFType


class Sgf(models.Model):
    """
    Model represents a single Smart Go Format file.
    """

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=SGFType.choices)
    sgf_file = models.FileField(upload_to="sgfs/")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plik SGF"
        verbose_name_plural = "Pliki SGF"
