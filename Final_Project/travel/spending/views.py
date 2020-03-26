from django.shortcuts import render, redirect, reverse
from .forms import *
from account.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from account.models import *


@login_required
def index(request):
    current_user = request.user
    user_trips = Trip.objects.filter(travelers__user=current_user)

    context = {'user': current_user, 'trips': user_trips}
    return render(request, 'spending/index.html', context)


@login_required
def finances(request, trip_id):
    current_user = request.user
    trip = Trip.objects.get(id=trip_id)
    purchases = Purchase.objects.filter(trip=trip)

    context = {'trip': trip, 'purchases': purchases}
    return render(request, 'spending/trip_finances.html', context)


@login_required
def add_purchase(request, trip_id):
    current_user = request.user
    trip = Trip.objects.get(id=trip_id)

    if request.method == 'POST':
        form = PurchaseModelForm(request.POST)

        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()

            for sharer in form.cleaned_data['sharers']:
                purchase.sharers.add(sharer)

            messages.success(request, "Purchase added!")
            return redirect('finances', trip_id)

    else:
        form = PurchaseModelForm()


    return render(request, 'spending/add_purchase.html', {'form': form})