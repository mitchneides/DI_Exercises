from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('parties/', parties, name='parties'),
    path('detail/<int:pk>', detail, name='detail'),
]
