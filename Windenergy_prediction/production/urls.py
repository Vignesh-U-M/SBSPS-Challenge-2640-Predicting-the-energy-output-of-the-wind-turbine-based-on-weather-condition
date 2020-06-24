from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('main', views.main, name="main"),
    path('map', views.map, name="map"),
    path('add_location_map', views.add_location_map, name="add_location_map")
]
