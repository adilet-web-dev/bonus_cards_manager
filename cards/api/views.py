from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from cards.models import Card
from cards.api.serializers import CardSerializer


class SearchCardListAPIView(ListAPIView):
    def list(self, request, *args, **kwargs):
        query = kwargs["query"]
        queryset = Card.objects.search(query)
        serializer = CardSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
