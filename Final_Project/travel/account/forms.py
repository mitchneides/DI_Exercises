from django.forms import *
from .models import *


class SignUpForm(Form):
    username = CharField(max_length=60, required=True, widget=TimeInput(
        {'class': 'form-control w-75'}))
    password = CharField(max_length=60, required=True, widget=PasswordInput(
        {'class': 'form-control w-75'}))
    email = EmailField(widget=EmailInput(
        {'class': 'form-control w-75'}))
    first_name = CharField(max_length=60, required=True, widget=TextInput(
        {'class': 'form-control w-75'}))
    last_name = CharField(max_length=60, required=True, widget=TextInput(
        {'class': 'form-control w-75'}))


class LoginForm(Form):
    username = CharField(max_length=60, required=True, widget=TimeInput(
        {'class': 'form-control w-75'}))
    password = CharField(max_length=60, required=True, widget=PasswordInput(
        {'class': 'form-control w-75'}))


class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'bio']
        widgets = {
            'bio': Textarea(attrs={'class': 'form-control'}),
            'picture': FileInput(attrs={'class': 'form-control'}),
        }


class JoinTripModelForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name']
        TRIP_CHOICES = [(trip.id, trip.name) for trip in Trip.objects.all()]
        widgets = {
                'name': SelectMultiple(choices=TRIP_CHOICES, attrs={'class': 'form-control'}),
        }


class DocumentModelForm(ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'image', 'profile']
        PROFILE_CHOICES = [profile for profile in Profile.objects.all()]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control'}),
            'profile': Select(attrs={'class': 'form-control'}),
        }




