from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('finances/trip_<int:trip_id>', views.finances, name='finances'),
    path('finances/add_purchase_<int:trip_id>', views.add_purchase, name='add_purchase'),

]