# studio/models.py
from django.db import models
from users.models import UserProfile

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

class Project(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

class PortfolioItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    media_file = models.FileField(upload_to='portfolio/')