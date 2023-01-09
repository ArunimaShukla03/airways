from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight")
]

# Here the flight id is created which will allow each flight to have a web page.