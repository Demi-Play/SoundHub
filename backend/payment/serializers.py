# payment/serializers.py
from rest_framework import serializers
from .models import PaymentMethod, Transaction
from users.serializers import UserProfileSerializer

class PaymentMethodSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = PaymentMethod
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'