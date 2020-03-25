from django.urls import path, re_path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('all_players/', views.all_players, name='all_players'),
    path('free_agents/', views.free_agents, name='free_agents'),
    path('my_team/', views.my_team, name='my_team'),
    path('rankings/', views.rankings, name='rankings'),
    path('trade_offers/', views.trade_offers, name='trade_offers'),
    path('quick_sell/<int:player_id>/', views.quick_sell, name='quick_sell'),
    path('quick_buy/<int:player_id>/', views.quick_buy, name='quick_buy'),
    path('trade_block/<int:player_id>/', views.trade_block, name='trade_block'),
    path('make_offer/<int:player_id>/', views.make_offer, name='make_offer'),
    path('answer_offer/<str:status>/<int:offer_id>/', views.answer_offer, name='answer_offer'),
]