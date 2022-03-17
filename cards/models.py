from django.db import models


class Card(models.Model):
    serial_number = models.IntegerField()
    number = models.IntegerField()
    created_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    amount = models.IntegerField()
    status = models.CharField(max_length=50)

