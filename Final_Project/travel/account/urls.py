from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit_profile', edit_profile, name='edit_profile'),
    path('profile/add_docs', add_docs, name='add_docs'),
    path('profile/delete_doc_<int:doc_id>', delete_doc, name='delete_doc'),
    path('site_plans', site_plans, name='site_plans'),

]