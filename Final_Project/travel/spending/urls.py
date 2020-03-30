from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('finances/trip_<int:trip_id>', views.finances, name='finances'),
    path('finances/add_purchase_<int:trip_id>', views.add_purchase, name='add_purchase'),
    path('finances/edit_purchase_<int:item_id>_<int:trip_id>', views.edit_purchase, name='edit_purchase'),
    path('finances/delete_purchase_<int:item_id>_<int:trip_id>', views.delete_purchase, name='delete_purchase'),
    path('finances/analytics_<int:trip_id>', views.analytics, name='analytics'),

]