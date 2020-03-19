from django.shortcuts import render, redirect, reverse
from account.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from trading.models import *


def index(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'account/index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                messages.warning(request, f'{form.cleaned_data["username"]} is already a user')
                return redirect(reverse('signup'))

            User.objects.create_user(**form.cleaned_data)
            messages.success(request, 'Signup successful!')
            return redirect(reverse('login'))

    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Welcome!')
                return redirect(reverse('profile'))
            else:
                messages.error(request, 'Invalid credentials')
                return redirect(reverse('login'))

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "Goodbye!")
    return redirect(reverse('login'))


@login_required
def profile(request):
    current_user = request.user
    user_id = current_user.id
    try:
        team = Team.objects.get(user_id=user_id)
    except:
        team = "You have not yet drafted your team."
        context = {'team': team}
    else:
        context = {'team': team}

    return render(request, 'account/profile.html', context=context)


