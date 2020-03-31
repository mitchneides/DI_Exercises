from django.contrib import admin
from .models import *


class DayPlanAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'trip')


admin.site.register(DayPlan, DayPlanAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'phone_number')


admin.site.register(Contact, ContactAdmin)