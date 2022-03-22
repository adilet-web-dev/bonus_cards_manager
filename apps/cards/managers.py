from django.db import models
from django.db.models import Q


class CardManager(models.Manager):
    def activated(self):
        return self.filter(_status="activated")

    def not_active(self):
        return self.filter(_status="not activated")

    def search(self, query: int):
        return self.filter(Q(serial_number=query) | Q(number=query))
