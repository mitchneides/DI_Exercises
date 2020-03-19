from django.forms import *
from film_app.models import *


boost = {'class': 'form-control'}


class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_date', 'country', 'category', 'director']
        widgets = {
            'title': TextInput(boost),
            'country': Select(boost),
            'director': Select(boost),
            'category': CheckboxSelectMultiple(),
            'release_date': DateInput({**boost, **{'type': 'date'}})
        }


class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        widgets = {
            'first_name': TextInput(boost),
            'last_name': TextInput(boost)
        }


class AddPosterForm(ModelForm):
    class Meta:
        model = Poster
        fields = '__all__'
