from django.urls import path
from . import views


urlpatterns = [
        path('', views.all_sightings),
        path('add/', views.add_sighting),
        #path("stats/", views.Stats),
        #path("<unique_squirrel_tracker_id>/", edit_sighting),
        ]
