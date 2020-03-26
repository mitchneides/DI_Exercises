from django.contrib import admin
from .models import *


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('item', 'description', 'category', 'price', 'datetime', 'buyer', 'trip')


admin.site.register(Purchase, PurchaseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)