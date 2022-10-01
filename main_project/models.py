from enum import auto
from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class ProjectRequest(models.Model):
    project_type = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.project_type

class Contact(models.Model):
    client_name = models.CharField(max_length=30)
    client_email = models.EmailField()
    client_mobile  = models.CharField(max_length=10)
    client_message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_contacted = models.BooleanField(default=False)
    

    def __str__(self):
        return self.client_name 