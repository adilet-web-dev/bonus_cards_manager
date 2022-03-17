import factory
from factory import fuzzy
from django.utils import timezone

from apps.cards.models import Card
from apps.payments.models import Payment


class PaymentFactory(factory.django.DjangoModelFactory):
    card = factory.SubFactory(Card)
    datetime = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    amount = fuzzy.FuzzyInteger(50, 5000)

    class Meta:
        model = Payment
