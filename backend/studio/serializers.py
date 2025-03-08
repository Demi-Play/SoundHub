# studio/serializers.py
from rest_framework import serializers
from .models import Equipment, Project, PortfolioItem
from users.serializers import UserProfileSerializer

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client = UserProfileSerializer()

    class Meta:
        model = Project
        fields = '__all__'

class PortfolioItemSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = PortfolioItem
        fields = '__all__'