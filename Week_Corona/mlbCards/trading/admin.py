from django.contrib import admin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'funds')


admin.site.register(Team, TeamAdmin)


class OfferAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, OfferAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'rank', 'team', 'price')


admin.site.register(Player, PlayerAdmin)

