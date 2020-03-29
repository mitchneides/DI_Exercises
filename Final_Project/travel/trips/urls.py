from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('new_trip/', views.new_trip, name='new_trip'),
    path('join_trip/', views.join_trip, name='join_trip'),
    path('add_destination/', views.add_destination, name='add_destination'),

]