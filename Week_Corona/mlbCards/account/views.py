from django.shortcuts import render, redirect, reverse
from account.forms import SignUpForm, LoginForm, CreateTeamForm
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
        team = ""
        players = ["Click 'Create Team' on the left side of the screen to begin.","Once your team has been set up, you can go to Trade Hub / Free Agents to purchase players and begin your dynasty!"]
        context = {'team': team, 'players': players}
    else:
        players = Player.objects.filter(team_id=team.id)
        if len(players) == 0:
            players = ["Go to Trade Hub / Free Agents to purchase players and begin your dynasty!"]
        context = {'team': team, 'players': players}

    return render(request, 'account/profile.html', context=context)


@login_required
def create_team(request):

    if request.method == 'POST':
        form = CreateTeamForm(request.POST)

        if form.is_valid():

            if Team.objects.filter(name=form.cleaned_data["team_name"]).exists():
                messages.warning(request, f'{form.cleaned_data["team_name"]} is already a team')
                return redirect(reverse('signup'))

            Team.objects.create(name=form.cleaned_data["team_name"], user=request.user)
            messages.success(request, 'Welcome to the league!')
            return redirect(reverse('profile'))

    else:
        form = CreateTeamForm()

    return render(request, 'account/create_team.html', {'form': form})


def view_competitor(request, team_id):
    team = Team.objects.get(id=team_id)
    players = Player.objects.filter(team=team).all()
    
    return render(request, 'account/view_competitor.html', context={'players': players, 'team': team})

