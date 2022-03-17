from rest_framework import serializers
from apps.cards.models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ["serial_number", "number", "created_at", "ends_at", "status", "amount"]
