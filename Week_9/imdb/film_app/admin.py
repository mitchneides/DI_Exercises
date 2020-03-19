from django.contrib import admin
from .models import Country, Category, Film, Director, Poster


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class FilmAdmin(admin.ModelAdmin):
    fields = ('title', 'director', 'category', 'country', 'poster')


admin.site.register(Film, FilmAdmin)


class DirectorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Director, DirectorAdmin)


class PosterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Poster, PosterAdmin)