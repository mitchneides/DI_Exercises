from django.forms import *
from .models import *


class PurchaseModelForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['item', 'description', 'category', 'price', 'datetime', 'buyer', 'sharers', 'trip']
        widgets = {
            'item': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'datetime': SelectDateWidget(attrs={'class': 'form-control'}),
            'buyer': Select(attrs={'class': 'form-control'}),
            'sharers': SelectMultiple(attrs={'class': 'form-control'}),
            'trip': Select(attrs={'class': 'form-control'}),
        }

