from django.db import models
from apps.cards.models import Card


class Payment(models.Model):
    card = models.ForeignKey(Card, related_name="payments", on_delete=models.PROTECT)
    datetime = models.DateTimeField()
    amount = models.PositiveIntegerField()
