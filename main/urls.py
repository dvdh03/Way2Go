from django.urls import path
from django.contrib import admin
from main import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Use CustomLoginView
    path('signup/', views.signup, name='signup'),
    path('destinations/', views.destination_list, name='destinations'),
    path('itineraries/', views.itinerary_list, name='itineraries'),
    path('about/', views.about, name='about'),
    path('start/', views.start, name='start'),
    path('home2/', views.home2_view, name='home2'),
    path('pla/', views.store_itinerary, name='store_itinerary'),
    path('ai/', views.ai, name='ai'),
    path('plan/', views.plan, name='plan'),
    path('generate/', views.generate_itinerary, name='generate_itinerary'),
    path('destination/<int:destination_id>/itinerary/', views.destination_itinerary, name='destination_itinerary'),
]