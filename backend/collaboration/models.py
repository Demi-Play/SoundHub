# collaboration/models.py
from django.db import models
from users.models import UserProfile
from studio.models import Project

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')
    version = models.CharField(max_length=20)

class CollaborationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_requests')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')