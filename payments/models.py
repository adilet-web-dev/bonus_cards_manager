from django.db import models


class Payment(models.Model):
    card = models.ForeignKey("cards.Card", related_name="payments", on_delete=models.PROTECT)
    datetime = models.DateTimeField()
    amount = models.PositiveIntegerField()
