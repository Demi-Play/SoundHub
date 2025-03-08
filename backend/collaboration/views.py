# collaboration/views.py
from rest_framework import viewsets
from .models import ProjectFile, CollaborationRequest
from .serializers import ProjectFileSerializer, CollaborationRequestSerializer

class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer

class CollaborationRequestViewSet(viewsets.ModelViewSet):
    queryset = CollaborationRequest.objects.all()
    serializer_class = CollaborationRequestSerializer