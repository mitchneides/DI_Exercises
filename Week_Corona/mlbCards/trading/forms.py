from django.forms import *
from django.forms import ModelForm
from .models import *


class OfferModelForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['money_amount', 'offering_players']
        OFFERING_PLAYERS_CHOICES = ()
        widgets = {
            'offering_players': SelectMultiple(choices=OFFERING_PLAYERS_CHOICES, attrs={'class': 'form-control'}),
        }