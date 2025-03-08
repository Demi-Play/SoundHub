# booking/models.py
from django.db import models
from studio.models import Equipment
from users.models import UserProfile

class BookingSlot(models.Model):
    equipment = models.ManyToManyField(Equipment)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slot = models.ForeignKey(BookingSlot, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)