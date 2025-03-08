# social_network/models.py
from django.db import models
from users.models import UserProfile

class MusicianProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    instruments = models.JSONField(default=list)
    genres = models.JSONField(default=list)
    experience_years = models.PositiveIntegerField(default=0)

class GroupProfile(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(UserProfile, related_name='groups')
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    organizer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)