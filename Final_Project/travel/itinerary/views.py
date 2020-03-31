from django.shortcuts import render, redirect, reverse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from account.models import *
from django.shortcuts import render


@login_required
def itin(request, trip_id):
    current_user = request.user
    trip = Trip.objects.get(id=trip_id)
    day_plans = DayPlan.objects.filter(trip=trip_id).order_by('date').all()

    context = {'user': current_user, 'trip': trip, 'dayplans': day_plans}
    return render(request, 'itinerary/itin.html', context)


@login_required
def add_dayplan(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip_contacts = Contact.objects.filter(trip=trip).all()

    if request.method == 'POST':
        form = DayPlanModelForm(request.POST)

        if form.is_valid():
            plan = form.save(commit=False)
            plan.trip = trip
            plan.save()

            for destination in form.cleaned_data['destinations']:
                plan.destinations.add(destination)

            for contact in form.cleaned_data['contacts']:
                plan.contacts.add(contact)

            for method in form.cleaned_data['transportation_methods']:
                plan.transportation_methods.add(method)

            messages.success(request, "Day plan added!")
            return redirect('itin', trip_id)

    else:
        form = DayPlanModelForm()

    return render(request, 'itinerary/add_dayplan.html', {'form': form, 'trip': trip})


def add_day_destination(request, trip_id):
    trip = Trip.objects.filter(id=trip_id)
    if request.method == 'POST':
        form = DayDestinationModelForm(request.POST)

        if form.is_valid():
            destination = form.save(commit=False)
            destination.save()

            messages.success(request, "Destination created")
            return redirect('add_dayplan', trip_id)

    else:
        form = DayDestinationModelForm()


    return render(request, 'itinerary/add_day_destination.html', {'form': form})


def add_contact(request, trip_id):
    trip = Trip.objects.filter(id=trip_id)
    if request.method == 'POST':
        form = ContactModelForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            messages.success(request, "Contact created")
            return redirect('add_dayplan', trip_id)

    else:
        form = ContactModelForm()


    return render(request, 'itinerary/add_contact.html', {'form': form})


@login_required
def edit_dayplan(request, trip_id, dayplan_id):
    trip = Trip.objects.get(id=trip_id)
    dayplan = DayPlan.objects.get(id=dayplan_id)

    if request.method == 'POST':
        form = DayPlanModelForm(request.POST, request.FILES, instance=dayplan)

        if form.is_valid():
            plan = form.save(commit=False)
            plan.trip = trip
            plan.save()

            for destination in form.cleaned_data['destinations']:
                plan.destinations.add(destination)

            for contact in form.cleaned_data['contacts']:
                plan.contacts.add(contact)

            for method in form.cleaned_data['transportation_methods']:
                plan.transportation_methods.add(method)

            messages.success(request, "Day plan added!")
            return redirect('itin', trip_id)

    else:
        form = DayPlanModelForm(instance=dayplan)

    return render(request, 'itinerary/add_dayplan.html', {'form': form, 'trip': trip})


@login_required
def delete_dayplan(request, trip_id, dayplan_id):
    trip = Trip.objects.get(id=trip_id)
    dayplan = DayPlan.objects.get(id=dayplan_id)

    dayplan.delete()
    messages.success(request, "Day/plan deleted")

    return redirect('itin', trip_id)
