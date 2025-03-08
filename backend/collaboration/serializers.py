# collaboration/serializers.py
from rest_framework import serializers
from .models import ProjectFile, CollaborationRequest
from studio.serializers import ProjectSerializer
from users.serializers import UserProfileSerializer

class ProjectFileSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    uploaded_by = UserProfileSerializer()

    class Meta:
        model = ProjectFile
        fields = '__all__'

class CollaborationRequestSerializer(serializers.ModelSerializer):
    sender = UserProfileSerializer()
    receiver = UserProfileSerializer()
    project = ProjectSerializer()

    class Meta:
        model = CollaborationRequest
        fields = '__all__'