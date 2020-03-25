from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(default='account/road.jpg', upload_to="account")
    bio = models.CharField(default='The highway sets the travelers stage; all exits look the same.', max_length=300, help_text='Enter a short bio/quote')

    def __str__(self):
        return self.user.username


class Trip(models.Model):
    name = models.CharField(max_length=80, help_text='Name your trip')
    travelers = models.ManyToManyField('Profile')
    destinations = models.ManyToManyField('Destination')
    start_date = models.DateField(blank=True, null=True, help_text='Useful but not required')
    end_date = models.DateField(blank=True, null=True, help_text='Useful but not required')
    completed = models.BooleanField(default=False)
    transportation_methods = models.ManyToManyField('Transportation', related_name='Travel_methods', blank=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
    city = models.CharField(blank=True, null=True, max_length=100, help_text='Useful but not required')
    state = models.CharField(blank=True, null=True, max_length=100, help_text='Useful but not required')
    country = models.CharField(max_length=100)

    def __str__(self):
        if self.city and self.state:
            return f"{self.city}/{self.state}/{self.country}"
        elif self.city:
            return f"{self.city}/{self.country}"
        elif self.state:
            return f"{self.state}/{self.country}"
        else:
            return self.country


class Transportation(models.Model):
    CHOICES = [
        ('A', 'Airplane'),
        ('Bu', 'Bus'),
        ('Bi', 'Bike'),
        ('C', 'Car'),
        ('H', 'Hike'),
        ('M', 'Motorcycle'),
        ('S', 'Ship'),
        ('T', 'Train'),
        ('W', 'Walk'),
    ]

    transportation_method = models.CharField(choices=CHOICES, default='C', max_length=2, help_text='Select any relevant')