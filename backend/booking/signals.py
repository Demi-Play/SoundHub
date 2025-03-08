# booking/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Booking

@receiver(post_save, sender=Booking)
def booking_status_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    data = {
        'id': instance.id,
        'status': instance.status,
        'start': instance.slot.start_time.isoformat(),
        'end': instance.slot.end_time.isoformat()
    }
    
    async_to_sync(channel_layer.group_send)(
        f"studio_{instance.slot.studio.id}_bookings",
        {
            'type': 'booking_update',
            'data': data
        }
    )