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

    context = {'trip': trip}
    return render(request, 'spending/trip_finances.html', context)