from django.shortcuts import render
from .models import Flight

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id) # more generic way of referencing a primary key.
    return render(request, "flights/flight.html", {
        "flight": flight
    })