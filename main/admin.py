from django.contrib import admin
from .models import ItineraryRequest, Destination, Itinerary

admin.site.register(ItineraryRequest) 
admin.site.register(Destination) 
admin.site.register(Itinerary) 