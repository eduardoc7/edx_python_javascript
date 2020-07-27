from django.shortcuts import render

from .models import Flight
# Create your views here.


def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})


def flight(request, flight_id):
    flight_details = Flight.objects.get(pk=flight_id) # aqui podendo também ser o flight_id do objeto | PK = primary key
    return render(request, "flights/flight.html", {
        "flight": flight_details
    })