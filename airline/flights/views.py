from django.shortcuts import render
from .models import Flight
from .models import Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id) # more generic way of referencing a primary key.
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

    # here passengers is our related name, it is a way of taking a flight and getting all of it's passengers.

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

        # when someone submits this form to book a new passenger on a flight then they should also tell me what the ID is of the passenger. 

        # So in order to get the new passenger name, we take the name from the user and convert it into an integer number while submitting this data in the "Passengers" model in order to add that passenger into the list of "Passengers".

        # After submitting the form we want the user to be redirected back to the flight page. Here we want the "flight" route as reverse takes the view and gets us the URL and it also takes an argument (here the "flight_id" which is structured as a tuple)