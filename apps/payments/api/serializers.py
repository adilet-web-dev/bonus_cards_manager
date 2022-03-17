from rest_framework.serializers import ModelSerializer

from apps.payments.models import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ["datetime", "amount"]