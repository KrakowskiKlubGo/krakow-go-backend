from django.db import models


class SGFType(models.TextChoices):
    TSUMEGO = "tsumego", "Tsumego"
    REVIEW = "review", "Review"
    CLUB_KNOWLEDGE = "club_knowledge", "Club Knowledge"
