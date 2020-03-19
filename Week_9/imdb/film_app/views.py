from django.shortcuts import render, redirect, reverse
from film_app.forms import *
from django.views.generic import CreateView, UpdateView
from django.contrib import messages



def index(request):
    return render(request, 'film_app/index.html')


def homepage(request):
    films = Film.objects.all()
    return render(request, 'film_app/homepage.html', {'films': films})


#generic class view simplifies code (compare to AddFilm below in comment)
class AddFilm(CreateView):
    form_class = AddFilmForm
    template_name = 'film_app/add_film.html'
    success_url = '/films/home'


class AddDirector(CreateView):
    form_class = AddDirectorForm
    template_name = 'film_app/add_director.html'
    success_url = '/films/home'


class AddPoster(CreateView):
    form_class = AddPosterForm
    template_name = 'film_app/add_poster.html'
    success_url = '/films/home'


class EditFilm(UpdateView):
    form_class = AddFilmForm
    template_name = 'film_app/add_film.html'
    success_url = '/films/home'

    # specify which film we are editing:
    def get_object(self, queryset=None):
        return Film.objects.get(pk=self.kwargs['pk'])


class EditDirector(UpdateView):
    form_class = AddDirectorForm
    template_name = 'film_app/add_director.html'
    success_url = '/films/home'

    # specify which director we are editing:
    def get_object(self, queryset=None):
        return Director.objects.get(pk=self.kwargs['pk'])



# Below not needed because of generic class views above

# def add_film(request):
#     if request.method == 'POST':
#         form = AddFilmForm(request.POST)
#
#         if form.is_valid():
#
#             if Film.objects.filter(title=form.cleaned_data["title"]).exists():
#                 messages.warning(request, f'{form.cleaned_data["title"]} is already in the database')
#                 return redirect(reverse('add_film'))
#
#             Film.create_film(**form.cleaned_data) #works because of custom function created in models
#             messages.success(request, 'Film successfully added!')
#             return redirect(reverse('add_film'))
#
#     else:
#         form = AddFilmForm()
#
#     return render(request, 'film_app/add_film.html', {'form': form})
#
#
# def add_director(request):
#     if request.method == 'POST':
#         form = AddDirectorForm(request.POST)
#
#         if form.is_valid():
#
#             if Director.objects.filter(last_name=form.cleaned_data["last_name"]).exists():
#                 if Director.objects.filter(first_name=form.cleaned_data["first_name"]).exists():
#                     messages.warning(request, f'{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]} is already in the database.')
#                     return redirect(reverse('add_director'))
#
#             Director.create_director(**form.cleaned_data) #works because of custom function created in models
#             messages.success(request, 'Director successfully added!')
#             return redirect(reverse('add_director'))
#
#     else:
#         form = AddDirectorForm()
#
#     return render(request, 'film_app/add_director.html', {'form': form})