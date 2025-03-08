# booking/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booking, BookingSlot
from .serializers import BookingSerializer, BookingSlotSerializer

class BookingSlotViewSet(viewsets.ModelViewSet):
    queryset = BookingSlot.objects.all()
    serializer_class = BookingSlotSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        slot = request.data.get('slot')
        if BookingSlot.objects.get(id=slot).is_booked:
            return Response({"error": "Slot already booked"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)