from django.shortcuts import render, redirect, reverse
from account_app.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

    return render(request, 'account_app/signup.html', {'form': form})


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

    return render(request, 'account_app/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "Goodbye!")
    return redirect(reverse('login'))


@login_required
def profile(request):
    return render(request, 'account_app/profile.html')