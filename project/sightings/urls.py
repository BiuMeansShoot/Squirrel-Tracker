from django.urls import path
from . import views


urlpatterns = [
        path('sightings/', views.all_sightings),
        path('sightings/add/', views.add_sightings),
        ]
