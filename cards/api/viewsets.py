from random import randint

from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.utils import timezone

from cards.models import Card
from .serializers import CardSerializer


class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    @action(methods=["post"], detail=True)
    def activate(self, request, pk=None):
        card = self.get_object()
        card.status = "activated"
        card.save()

        return Response(status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        for i in range(int(data["quantity"])):
            card = self.serializer_class(data={
                "serial_number": data["serial_number"],
                "number": randint(10_000, 99_999),
                "created_at": timezone.now(),
                "ends_at": data["ends_at"],
                "amount": 0,
                "status": "not activated"
            })
            if card.is_valid():
                card.save()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
