from django.forms import *
from account.models import *
from .models import *


class DayPlanModelForm(ModelForm):
    class Meta:
        model = DayPlan
        fields = ['date', 'name', 'destinations', 'requirements', 'contacts', 'transportation_methods', 'journal']
        widgets = {
            'date': SelectDateWidget(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'destinations': SelectMultiple(attrs={'class': 'form-control'}),
            'requirements': Textarea(attrs={'class': 'form-control'}),
            'contacts': SelectMultiple(attrs={'class': 'form-control'}),
            'transportation_methods': SelectMultiple(attrs={'class': 'form-control'}),
            'journal': Textarea(attrs={'class': 'form-control'}),

        }


class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'company', 'phone_number', 'trip']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'company': TextInput(attrs={'class': 'form-control'}),
            'phone_number': TextInput(),
            'trip': Select(attrs={'class': 'form-control'}),
        }


class DayDestinationModelForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['city', 'state', 'country']
        widgets = {
            'city': TextInput(attrs={'class': 'form-control'}),
            'state': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
        }

