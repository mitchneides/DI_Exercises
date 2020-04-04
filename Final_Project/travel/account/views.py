from django.shortcuts import render, redirect, reverse
from account.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def index(request):
    return render(request, 'account/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():

            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                messages.warning(request, f'{form.cleaned_data["username"]} is already a user')
                return redirect(reverse('signup'))

            new_user = User.objects.create_user(**form.cleaned_data)

            Profile.objects.create(user=new_user)

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
    profile_info = Profile.objects.get(user=current_user)
    docs = Document.objects.filter(profile=profile_info).all()

    context = {'user': current_user, 'info': profile_info, 'docs': docs}

    return render(request, 'account/profile.html', context=context)


@login_required
def edit_profile(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        # instance=user_profile -> points to the existing object
        form = ProfileModelForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')
            return redirect(reverse('profile'))

    else:
        form = ProfileModelForm(instance=user_profile)

    return render(request, 'account/edit_profile.html', {'form': form})


@login_required
def add_docs(request):
    current_user = request.user
    user_profile = Profile.objects.get(user=current_user)

    if request.method == 'POST':
        # instance=user_profile -> points to the existing object
        form = DocumentModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Document successfully added!')
            return redirect(reverse('profile'))

    else:
        form = DocumentModelForm()

    return render(request, 'account/add_docs.html', {'form': form})


@login_required
def delete_doc(request, doc_id):
    doc = Document.objects.get(id=doc_id)

    doc.profile_id = None
    doc.save()

    return redirect(reverse('profile'))




