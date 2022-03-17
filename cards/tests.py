from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework import status
from cards.factories import CardFactory
from cards.models import Card


class CardViewSetTest(APITestCase):
    def test_it_creates_card(self):
        payload = {
            "serial_number": 123,
            "quantity": 10,
            "ends_at": timezone.now() + timezone.timedelta(days=10)
        }

        response = self.client.post("/api/v1/cards/", payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_cards = Card.objects.filter(serial_number=payload["serial_number"])
        self.assertEqual(created_cards.count(), payload["quantity"])

    def test_it_deletes_card(self):
        card = CardFactory()
        self.client.delete(f"/api/v1/cards/{card.id}/")

        self.assertFalse(Card.objects.filter(id=card.id).exists())

    def test_it_activates_card(self):
        card = CardFactory(status="not activated")
        response = self.client.post(f"/api/v1/cards/{card.id}/activate/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        card.refresh_from_db()
        self.assertEqual(card.status, "activated")


class CardListAPITest(APITestCase):
    def test_it_responses_card_list(self):
        CardFactory.create_batch(3)
        response = self.client.get("/api/v1/cards/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)



