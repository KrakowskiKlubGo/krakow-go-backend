from django.db import models

from sgfs.const import SGFType


class Sgf(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=SGFType.choices)
    sgf_file = models.FileField(upload_to="sgfs/")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
