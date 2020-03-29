from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from account.models import *
from account.forms import *


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
            return redirect('/trips/')

    else:
        form = TripModelForm()

    return render(request, 'trips/new_trip.html', {'form': form})


@login_required
def join_trip(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)
    all_trips = Trip.objects.all()

    if request.method == 'POST':
        form = JoinTripModelForm(request.POST)

        if form.is_valid():
            form.save(commit=False)

            for trip in form.cleaned_data['name']:
                print(trip)
                if trip.isdigit():
                    trip_ob = Trip.objects.get(id=trip)
                    trip_ob.travelers.add(user_profile)
                    trip_ob.save()

            messages.success(request, "Trip joined!")
            return redirect('/trips/')

    else:
        form = JoinTripModelForm()
        form.fields['name'].choices = [(trip.id, trip.name) for trip in all_trips]

    return render(request, 'trips/join_trip.html', {'form': form})


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


