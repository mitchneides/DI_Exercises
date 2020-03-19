from django.urls import path, re_path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]