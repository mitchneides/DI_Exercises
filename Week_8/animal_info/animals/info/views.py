from django.shortcuts import render
from django.http import HttpResponse
from . import models



def info(request):
    return render(request, template_name='info.html')


def animal(request, num):
    animal_1 = models.Animal.object.filter(id=num)
    print(animal_1)
    return render(request, template_name='animal.html', context={'animal': animal_1})


def family(request):
    return render(request, template_name='family.html')



# def parties(request):
#     parties = ["Likud", "Blue&White", "Emet", "Shas", "Joint-list", "Yemina", "Israel-Beitenu", "Otzma"]
#     return render(request, template_name='app/parties.html', context={'parties': parties})
