# social_network/views.py
from rest_framework import viewsets
from .models import MusicianProfile, GroupProfile, Event
from .serializers import MusicianProfileSerializer, GroupProfileSerializer, EventSerializer

class MusicianProfileViewSet(viewsets.ModelViewSet):
    queryset = MusicianProfile.objects.all()
    serializer_class = MusicianProfileSerializer

class GroupProfileViewSet(viewsets.ModelViewSet):
    queryset = GroupProfile.objects.all()
    serializer_class = GroupProfileSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer