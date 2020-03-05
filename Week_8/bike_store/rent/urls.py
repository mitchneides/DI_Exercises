from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('customer/', customer, name='customer'),
    path('vehicle/', vehicle, name='vehicle'),
    path('rental/', rental, name='rental'),
]
