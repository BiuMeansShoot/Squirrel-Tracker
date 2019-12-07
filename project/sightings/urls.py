from django.urls import path
from . import views


urlpatterns = [
        path('', views.all_sightings),
        path('add/', views.add_sighting),
        path("stats/", views.sightingsStats),
        path("<int:unique_id>/", views.edit_sighting),
        ]
