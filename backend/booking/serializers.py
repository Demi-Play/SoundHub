# booking/serializers.py
from rest_framework import serializers
from .models import Booking, BookingSlot
from studio.serializers import EquipmentSerializer
from users.serializers import UserProfileSerializer

class BookingSlotSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer(many=True)

    class Meta:
        model = BookingSlot
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    slot = BookingSlotSerializer()

    class Meta:
        model = Booking
        fields = '__all__'