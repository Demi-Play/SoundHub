# collaboration/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import CollaborationRequest, ProjectFile

class CollaborationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.room_group_name = f"project_{self.project_id}"
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['type'] == 'new_request':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'collaboration_message',
                    'message': data['message']
                }
            )

    async def collaboration_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))