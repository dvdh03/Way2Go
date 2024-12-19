
from main.models import Destination, Itinerary

# Dummy Destinations
dummy_destinations = [
    {"name": "Paris", "description": "The city of light and love.", "image": None},
    {"name": "Maldives", "description": "A tropical paradise with crystal clear waters.", "image": None},
    {"name": "Switzerland", "description": "Snow-capped mountains and scenic beauty.", "image": None},
    {"name": "Tokyo", "description": "A blend of tradition and technology.", "image": None},
    {"name": "Dubai", "description": "Luxury and modern architecture.", "image": None},
    {"name": "Rome", "description": "The eternal city with historical landmarks.", "image": None},
    {"name": "London", "description": "A cultural and financial hub.", "image": None},
    {"name": "Bali", "description": "An Indonesian island known for its forests and beaches.", "image": None},
    {"name": "Singapore", "description": "A melting pot of cultures and modernity.", "image": None},
    {"name": "Bangkok", "description": "A vibrant city with amazing street food.", "image": None},
    {"name": "Hong Kong", "description": "Skyline views and bustling markets.", "image": None},
    {"name": "Barcelona", "description": "A city of art and architecture.", "image": None},
]

# Dummy Itineraries
dummy_itineraries = {
    "Paris": [
        {
            "title": "Romantic Day in Paris",
            "highlights": "Eiffel Tower,Seine River Cruise,Louvre Museum",
            "details": "Spend a romantic day exploring iconic landmarks like the Eiffel Tower and Louvre Museum.",
        },
        {
            "title": "Art and History Tour",
            "highlights": "Montmartre,Orsay Museum,Notre-Dame Cathedral",
            "details": "Immerse yourself in Parisian art and history with a day exploring Montmartre and Notre-Dame.",
        },
    ],
    "Maldives": [
        {
            "title": "Island Hopping Adventure",
            "highlights": "Snorkeling,Private Island Tour,Dolphin Watching",
            "details": "Discover the Maldives by hopping between islands and enjoying its underwater wonders.",
        },
        {
            "title": "Luxury Retreat",
            "highlights": "Resort Spa,Gourmet Dining,Sunset Cruise",
            "details": "Relax in luxury with world-class dining and rejuvenating spa treatments.",
        },
    ],
    "Switzerland": [
        {
            "title": "Alpine Wonders",
            "highlights": "Jungfraujoch,Interlaken,Zermatt",
            "details": "Experience the breathtaking beauty of the Swiss Alps and iconic mountain villages.",
        },
        {
            "title": "Lakes and Cities",
            "highlights": "Lake Geneva,Lake Zurich,Lugano",
            "details": "Discover Switzerland’s stunning lakes and vibrant cities like Zurich and Geneva.",
        },
    ],
    "Tokyo": [
        {
            "title": "City Lights and Culture",
            "highlights": "Shibuya Crossing,Tokyo Skytree,Meiji Shrine",
            "details": "Explore Tokyo’s vibrant city life and traditional cultural landmarks.",
        },
        {
            "title": "Nature and Serenity",
            "highlights": "Ueno Park,Senso-ji Temple,Mount Fuji",
            "details": "Find peace in Tokyo’s serene parks and temples, and enjoy a day trip to Mount Fuji.",
        },
    ],
    "Dubai": [
        {
            "title": "Modern Dubai",
            "highlights": "Burj Khalifa,Dubai Mall,Dubai Marina",
            "details": "Explore Dubai’s luxurious lifestyle and iconic modern landmarks.",
        },
        {
            "title": "Desert Safari",
            "highlights": "Camel Ride,Sandboarding,BBQ Dinner",
            "details": "Experience the Arabian Desert with an adventurous safari and cultural evening.",
        },
    ],
    "Rome": [
        {
            "title": "Ancient Rome Tour",
            "highlights": "Colosseum,Palatine Hill,Roman Forum",
            "details": "Walk through ancient Roman history with visits to iconic landmarks.",
        },
        {
            "title": "Vatican and Art",
            "highlights": "Vatican Museums,Sistine Chapel,St. Peter’s Basilica",
            "details": "Marvel at the art and architecture of the Vatican.",
        },
    ],
    "London": [
        {
            "title": "Historic London",
            "highlights": "Tower of London,Buckingham Palace,Westminster Abbey",
            "details": "Step back in time and explore London’s royal history and iconic landmarks.",
        },
        {
            "title": "Cultural Day Out",
            "highlights": "British Museum,Tate Modern,London Eye",
            "details": "Discover London’s art and culture with visits to museums and the iconic London Eye.",
        },
    ],
    "Bali": [
        {
            "title": "Beach Paradise",
            "highlights": "Kuta Beach,Seminyak,Uluwatu Temple",
            "details": "Relax on Bali’s stunning beaches and explore its spiritual side at Uluwatu Temple.",
        },
        {
            "title": "Nature and Adventure",
            "highlights": "Mount Batur,Rice Terraces,Ubud Monkey Forest",
            "details": "Embark on an adventure to Bali’s volcanic mountains and lush rice terraces.",
        },
    ],
    "Singapore": [
        {
            "title": "City Highlights",
            "highlights": "Marina Bay Sands,Gardens by the Bay,Merlion",
            "details": "Explore Singapore’s iconic cityscape and lush gardens.",
        },
        {
            "title": "Cultural Exploration",
            "highlights": "Chinatown,Little India,Kampong Glam",
            "details": "Dive into Singapore’s diverse cultural neighborhoods.",
        },
    ],
    "Bangkok": [
        {
            "title": "Temples and Palaces",
            "highlights": "Grand Palace,Wat Arun,Wat Pho",
            "details": "Discover Bangkok’s rich cultural and spiritual heritage.",
        },
        {
            "title": "Street Food and Markets",
            "highlights": "Chatuchak Market,Floating Market,Khao San Road",
            "details": "Indulge in Bangkok’s world-famous street food and vibrant markets.",
        },
    ],
    "Hong Kong": [
        {
            "title": "Skyline Views",
            "highlights": "Victoria Peak,Star Ferry,Avenue of Stars",
            "details": "Experience Hong Kong’s iconic skyline and waterfront.",
        },
        {
            "title": "Cultural Hong Kong",
            "highlights": "Man Mo Temple,Wong Tai Sin Temple,Temple Street Night Market",
            "details": "Discover the cultural heritage and bustling markets of Hong Kong.",
        },
    ],
    "Barcelona": [
        {
            "title": "Architectural Marvels",
            "highlights": "Sagrada Familia,Park Güell,Casa Batlló",
            "details": "Explore Barcelona’s stunning architecture by Gaudí.",
        },
        {
            "title": "Historic Walks",
            "highlights": "Gothic Quarter,La Rambla,Barcelona Cathedral",
            "details": "Stroll through Barcelona’s historic streets and landmarks.",
        },
    ],
}

# Script to populate data
for dest in dummy_destinations:
    destination = Destination.objects.create(
        name=dest["name"],
        description=dest["description"],
        image=dest["image"],  # Add an image path if available
    )
    
    if destination.name in dummy_itineraries:
        for itinerary_data in dummy_itineraries[destination.name]:
            Itinerary.objects.create(
                destination=destination,
                title=itinerary_data["title"],
                highlights=itinerary_data["highlights"],
                details=itinerary_data["details"],
                image=None,  # Add an image path if available
            )
