# social_network/serializers.py
from rest_framework import serializers
from .models import MusicianProfile, GroupProfile, Event
from users.serializers import UserProfileSerializer

class MusicianProfileSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = MusicianProfile
        fields = '__all__'

class GroupProfileSerializer(serializers.ModelSerializer):
    members = UserProfileSerializer(many=True)

    class Meta:
        model = GroupProfile
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    organizer = UserProfileSerializer()

    class Meta:
        model = Event
        fields = '__all__'