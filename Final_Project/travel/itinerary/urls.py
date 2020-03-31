from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('trip_<int:trip_id>', views.itin, name='itin'),
    path('add_dayplan/trip_<int:trip_id>', views.add_dayplan, name='add_dayplan'),
    path('add_day_destination_<int:trip_id>', views.add_day_destination, name='add_day_destination'),
    path('add_contact_<int:trip_id>', views.add_contact, name='add_contact'),
    path('edit_dayplan_<int:trip_id>_<int:dayplan_id>', views.edit_dayplan, name='edit_dayplan'),
    path('delete_dayplan_<int:trip_id>_<int:dayplan_id>', views.delete_dayplan, name='delete_dayplan'),

]