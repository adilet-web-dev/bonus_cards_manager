from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework import status

from apps.cards.factories import CardFactory
from apps.cards.models import Card
from apps.users.factories import UserFactory
from apps.payments.factories import PaymentFactory


class CardTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_it_creates_card(self):
        payload = {
            "serial_number": 123,
            "quantity": 10,
            "ends_at": timezone.now() + timezone.timedelta(days=10),
        }

        response = self.client.post("/api/v1/cards/", payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_cards = Card.objects.filter(serial_number=payload["serial_number"])
        self.assertEqual(created_cards.count(), payload["quantity"])

    def test_it_deletes_card(self):
        card = CardFactory()
        self.client.delete(f"/api/v1/cards/{card.id}/")

        self.assertFalse(Card.objects.filter(id=card.id).exists())

    def test_it_responses_card_list(self):
        CardFactory.create_batch(3)
        response = self.client.get("/api/v1/cards/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CardActivationTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_it_activates_card(self):
        card = CardFactory(status="not activated")
        response = self.client.post(f"/api/v1/cards/{card.id}/activate/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        card.refresh_from_db()
        self.assertEqual(card.status, "activated")

    def test_it_deactivates_card(self):
        card = CardFactory(status="activated")
        response = self.client.post(f"/api/v1/cards/{card.id}/deactivate/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        card.refresh_from_db()
        self.assertEqual(card.status, "not activated")

    def test_it_responses_active_cards(self):
        CardFactory.create_batch(3, status="activated")
        CardFactory.create_batch(2, status="not activated")

        response = self.client.get("/api/v1/cards/active/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_it_responses_inactive_cards(self):
        CardFactory.create_batch(3, status="activated")
        CardFactory.create_batch(2, status="not activated")

        response = self.client.get("/api/v1/cards/inactive/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_card_activity_representation(self):
        card = CardFactory(ends_at=timezone.now() - timezone.timedelta(days=3))
        response = self.client.get(f"/api/v1/cards/{card.id}/")
        self.assertEqual(response.data["status"], "not activated")

        card = CardFactory(ends_at=timezone.now() + timezone.timedelta(days=3))
        response = self.client.get(f"/api/v1/cards/{card.id}/")
        self.assertEqual(response.data["status"], "expired")


class SearchCardTest(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/v1/cards/search={}"
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_it_finds_by_serial_number(self):
        card = CardFactory()

        response = self.client.get(self.url.format(card.serial_number))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, card.serial_number)

    def test_it_finds_by_number(self):
        card = CardFactory()

        response = self.client.get(self.url.format(card.number))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, card.number)


class CardHistoryTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_it_shows_card_history(self):
        card = CardFactory()
        payments: list = PaymentFactory.create_batch(3, card=card)

        response = self.client.get(f"/api/v1/cards/{card.id}/payments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, payments[0].amount)
        self.assertContains(response, payments[1].amount)
        self.assertContains(response, payments[2].amount)
