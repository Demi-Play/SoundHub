from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import CollaborationRequest, ProjectFile

@receiver(post_save, sender=CollaborationRequest)
def send_collaboration_notification(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{instance.receiver.user.id}",
        {
            'type': 'collaboration_update',
            'data': {
                'message': f"New collaboration request from {instance.sender.user.username}",
                'project_id': instance.project.id
            }
        }
    )