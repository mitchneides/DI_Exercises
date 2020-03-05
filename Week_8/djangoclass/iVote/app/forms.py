from django.forms import Form
from django.forms import ChoiceField
from app.models import Affiliation


CHOICES = [(aff.name, aff.name) for aff in Affiliation.objects.all()]
CHOICES += [('all', 'All')]


class FilterForm(Form):
    affiliation = ChoiceField(choices=CHOICES)
