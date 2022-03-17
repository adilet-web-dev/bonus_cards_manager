from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.cards.models import Card
from apps.cards.api.serializers import CardSerializer


class SearchCardListAPIView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        query = kwargs["query"]
        queryset = Card.objects.search(query)
        serializer = CardSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
