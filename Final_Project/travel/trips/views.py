from django.shortcuts import render, redirect, reverse
from .forms import *
from account.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from account.models import *


def index(request):
    return render(request, 'trips/index.html')