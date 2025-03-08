# payment/views.py
from rest_framework import viewsets
from .models import PaymentMethod, Transaction
from .serializers import PaymentMethodSerializer, TransactionSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer