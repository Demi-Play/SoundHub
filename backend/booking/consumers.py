# booking/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Booking, BookingSlot

class BookingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.studio_id = self.scope['url_route']['kwargs']['studio_id']
        self.room_group_name = f"studio_{self.studio_id}_bookings"
        
        # Проверка прав доступа
        if not self.scope['user'].is_authenticated:
            await self.close()
            return

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        await self.send_initial_data()

    async def send_initial_data(self):
        bookings = Booking.objects.filter(slot__studio_id=self.studio_id)
        serialized = []
        for booking in bookings:
            serialized.append({
                'id': booking.id,
                'start': booking.slot.start_time.isoformat(),
                'end': booking.slot.end_time.isoformat(),
                'user': booking.user.user.username
            })
        await self.send(text_data=json.dumps({
            'type': 'INITIAL_DATA',
            'data': serialized
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['type'] == 'BOOKING_CREATE':
            # Здесь может быть логика создания брони через WebSocket
            pass

    async def booking_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'BOOKING_UPDATE',
            'data': event['data']
        }))