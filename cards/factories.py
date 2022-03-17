import factory
from factory import fuzzy
from cards.models import Card
import random


class CardFactory(factory.django.DjangoModelFactory):
    serial_number = fuzzy.FuzzyInteger(100, 999)
    number = fuzzy.FuzzyInteger(1000)
    created_at = factory.Faker("date_time")
    ends_at = factory.Faker("date_time")
    amount = fuzzy.FuzzyInteger(10_000)

    class Meta:
        model = Card
