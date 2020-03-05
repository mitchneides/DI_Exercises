from . import views
from django.urls import path

urlpatterns = [
    path('', views.info, name='info'),
    path('animal/<num>', views.animal, name="animal"),
    path('family/<num>', views.family, name="family"),
    
]
