from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import *


@login_required
def index(request):
    current_user = request.user
    user_trips = Trip.objects.filter(travelers__user=current_user)

    context = {'user': current_user, 'trips': user_trips}
    return render(request, 'trips/index.html', context)


@login_required
def new_trip(request):

    if request.method == 'POST':
        form = TripModelForm(request.POST)

        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()

            for traveler in form.cleaned_data['travelers']:
                trip.travelers.add(traveler)

            for destination in form.cleaned_data['destinations']:
                trip.destinations.add(destination)

            for transportation_method in form.cleaned_data['transportation_methods']:
                trip.transportation_methods.add(transportation_method)

            messages.success(request, "Trip created! Let's get planning!")
            return redirect(reverse('profile'))

    else:
        form = TripModelForm()


    return render(request, 'trips/new_trip.html', {'form': form})


def add_destination(request):
    if request.method == 'POST':
        form = DestinationModelForm(request.POST)

        if form.is_valid():
            destination = form.save(commit=False)
            destination.save()

            messages.success(request, "Destination created")
            return redirect(reverse('new_trip'))

    else:
        form = DestinationModelForm()


    return render(request, 'trips/add_destination.html', {'form': form})


