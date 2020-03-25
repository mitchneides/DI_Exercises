from django.forms import *
from account.models import *
from .models import *


class TripModelForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'travelers', 'destinations', 'start_date', 'end_date', 'status', 'transportation_methods']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'travelers': SelectMultiple(attrs={'class': 'form-control'}),
            'destinations': SelectMultiple(attrs={'class': 'form-control'}),
            'start_date': SelectDateWidget(attrs={'class': 'form-control'}),
            'end_date': SelectDateWidget(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
            'transportation_methods': SelectMultiple(attrs={'class': 'form-control'}),
        }


class DestinationModelForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['city', 'state', 'country']
        widgets = {
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
        }


