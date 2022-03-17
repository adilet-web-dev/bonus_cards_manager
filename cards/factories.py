import factory
from factory import fuzzy
from django.utils import timezone

from cards.models import Card


class CardFactory(factory.django.DjangoModelFactory):
    serial_number = fuzzy.FuzzyInteger(100, 999)
    number = fuzzy.FuzzyInteger(1000)
    created_at = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    ends_at = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    amount = fuzzy.FuzzyInteger(10_000)

    class Meta:
        model = Card
