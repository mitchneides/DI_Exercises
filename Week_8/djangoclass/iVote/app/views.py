from django.shortcuts import render
from app.models import Party
from app.forms import FilterForm

# Create your views here.


def index(request):
    return render(request, template_name='app/index.html')


def parties(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            aff = form.cleaned_data['affiliation']
            if aff == 'all':
                p_names = Party.objects.all()
            else:
                p_names = Party.objects.filter(affiliation__name=aff) #returns a list of party names that have the selected affiliation
    else:
        form = FilterForm()
        p_names = Party.objects.all()

    return render(request, template_name='app/parties.html', context={'parties': p_names, 'form': form})


def detail(request,pk): #pk=primary key

    party = Party.objects.get(pk=pk)

    return render(request, 'app/detail.html', {'party': party})




