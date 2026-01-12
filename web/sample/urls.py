from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("clicked", views.clicked, name="clicked"),
    path("map/", views.map_view, name="map"),
    path("validate_pin/", views.validate_pin, name="validate_pin"),
    path("submit_location/", views.submit_location, name="submit_location"),
]
