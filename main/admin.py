from django.contrib import admin
from .models import ItineraryRequest, Destination, Itinerary

@admin.register(ItineraryRequest)
class ItineraryRequestAdmin(admin.ModelAdmin):
    list_display = ("username", "budget", "climate", "group_size", "duration", "start_date", "end_date", "created_at")
    search_fields = ("climate", "interests")
    list_filter = ("climate", "created_at")

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "destination", "created_at")
    search_fields = ("title", "destination__name")
    list_filter = ("destination", "created_at")