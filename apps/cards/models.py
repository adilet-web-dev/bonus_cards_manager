from django.db import models
from django.utils import timezone

from apps.cards.managers import CardManager


class Card(models.Model):
    serial_number = models.IntegerField()
    number = models.IntegerField()
    created_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    amount = models.IntegerField()
    _status = models.CharField(max_length=50, default="not activated")

    @property
    def status(self):
        return self._status

    @status.getter
    def status(self):
        if self.ends_at <= timezone.now():
            return "expired"
        else:
            return self._status

    @status.setter
    def status(self, value):
        self._status = value

    objects = CardManager()
