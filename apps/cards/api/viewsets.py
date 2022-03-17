from random import randint

from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.db.models import QuerySet

from apps.cards.models import Card
from .serializers import CardSerializer
from apps.payments.api.serializers import PaymentSerializer


class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    permission_classes = [IsAuthenticated]

    @action(methods=["post"], detail=True)
    def activate(self, request, pk=None):
        self.set_status("activated")

        return Response(status=status.HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def deactivate(self, request, pk=None):
        self.set_status("not activated")

        return Response(status=status.HTTP_200_OK)

    def set_status(self, status: str):
        card = self.get_object()
        card.status = status
        card.save()

    @action(methods=["get"], detail=False, url_path="active")
    def get_active_cards(self, request):
        data = self.get_many_data(Card.objects.activated())
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False, url_path="inactive")
    def get_inactive_cards(self, request):
        data = self.get_many_data(Card.objects.not_active())
        return Response(data=data, status=status.HTTP_200_OK)

    def get_many_data(self, queryset: QuerySet):
        return self.serializer_class(queryset, many=True).data

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        for i in range(int(data["quantity"])):
            card = self.serializer_class(
                data={
                    "serial_number": data["serial_number"],
                    "number": randint(10_000, 99_999),
                    "created_at": timezone.now(),
                    "ends_at": data["ends_at"],
                    "amount": 0,
                    "status": "not activated",
                }
            )
            if card.is_valid():
                card.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True, url_path="payments")
    def payments_history(self, request, *args, **kwargs):
        card: Card = self.get_object()
        payments = card.payments.all()

        serializer = PaymentSerializer(payments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
