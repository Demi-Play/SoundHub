from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/studio/(?P<studio_id>\d+)/$', consumers.BookingConsumer.as_asgi()),
]