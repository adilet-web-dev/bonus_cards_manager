from django.db import models
from django.utils import timezone

from apps.cards.managers import CardManager


class Card(models.Model):
    serial_number = models.IntegerField()
    number = models.IntegerField()
    created_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default="not activated")

    objects = CardManager()