from django.db import models
from django.contrib.auth.models import User

# ChatMessage model
class ChatMessage(models.Model):
    sender = models.CharField(max_length=10)  # 'user' or 'bot'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:50]}"

# Booking model
class Booking(models.Model):
    service = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=200, default="General Consultation")  # Default value
    consultant = models.CharField(max_length=100, default="Not Assigned")  # Default value

    def __str__(self):
        return f"{self.service} on {self.date} at {self.time}"