from django.db import models
from django.contrib.auth.models import User

class ItineraryRequest(models.Model):
    username = models.CharField(max_length=150)
    budget = models.IntegerField()
    climate = models.CharField(max_length=50)
    interests = models.TextField()  # Stores interests as a comma-separated string
    group_size = models.IntegerField()
    duration = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    response = models.TextField()  # Stores the AI-generated response

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Itinerary for {self.username} - {self.start_date} to {self.end_date}"

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)   
    description = models.TextField(blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="itineraries")
    title = models.CharField(max_length=200)
    highlights = models.TextField()   
    details = models.TextField()   
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.destination.name} - {self.title}"