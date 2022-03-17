from django.db import models


class Card(models.Model):
    serial_number = models.IntegerField(max_length=999)
    created_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    amount = models.IntegerField()
    status = models.CharField(
        max_length=50,
        choices=["not activated", "activated", "expired"]
    )
