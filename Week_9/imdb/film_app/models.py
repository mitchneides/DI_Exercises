from django.db import models
from django.db.models import *
from datetime import date


class Country(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']


class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default=date.today)
    country = models.ForeignKey(Country, on_delete=SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    director = models.ForeignKey('Director', on_delete=SET_NULL, null=True)
    poster = models.OneToOneField('Poster', on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'

    def categories(self):
        return ', '.join([cat.name for cat in self.category.all()])

    class Meta:
        ordering = ['title']

    # def create_film(self, *args):
    #     f = Film(*args)
    #     f.save()


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name']

    # def create_director(self, first, last):
    #     d = Director(first_name=first, last_name=last)
    #     d.save()


class Poster(models.Model):
    image = models.ImageField(upload_to='static/images/', null=True)
    explanation_text = models.CharField(max_length=200)
