from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', homepage, name='home'),
    path('add_film/', AddFilm.as_view(), name='addfilm'),
    path('add_director/', AddDirector.as_view(), name='add_director'),
    path('add_poster/', AddPoster.as_view(), name='add_poster'),
    path('editfilm/<int:pk>', EditFilm.as_view(), name='editfilm'),
    path('editdirector/<int:pk>', EditDirector.as_view(), name='editdirector'),
]