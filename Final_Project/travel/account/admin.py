from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture', 'bio')


admin.site.register(Profile, ProfileAdmin)


class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date')


admin.site.register(Trip, TripAdmin)


class DestinationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'country')


admin.site.register(Destination, DestinationAdmin)


class TransportationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Transportation, TransportationAdmin)