from django.db import models
from django.db.models import Q


class CardManager(models.Manager):
    def activated(self):
        return self.filter(status="activated")

    def not_active(self):
        return self.filter(status="not activated")

    def search(self, query: int):
        return self.filter(Q(serial_number=query) | Q(number=query))
