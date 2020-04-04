from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(default='account/road.jpg', upload_to="account")
    bio = models.CharField(default='The highway sets the travelers stage; all exits look the same.', max_length=300, help_text='Enter a short bio/quote')

    def __str__(self):
        return self.user.username


class Trip(models.Model):
    name = models.CharField(max_length=80)
    travelers = models.ManyToManyField('Profile', help_text='Who will be traveling on this journey?')
    destinations = models.ManyToManyField('Destination', help_text='Ctrl + click to select multiple')
    start_date = models.DateField(blank=True, null=True, help_text='Useful but not required')
    end_date = models.DateField(blank=True, null=True, help_text='Useful but not required')

    CHOICES = [
        ('Done', 'Trip has been completed'),
        ('Open', 'Trip is ongoing')
    ]
    status = models.CharField(choices=CHOICES, default='Open', max_length=4)

    transportation_methods = models.ManyToManyField('Transportation', related_name='Travel_methods', blank=True, help_text='Ctrl + click to select multiple')

    def __str__(self):
        return self.name


class Destination(models.Model):
    city = models.CharField(blank=True, null=True, max_length=100, help_text='Useful but not required')
    state = models.CharField(blank=True, null=True, max_length=100, help_text='Useful but not required')
    country = models.CharField(max_length=100)

    def __str__(self):
        if self.city and self.state:
            return f"{self.city}, {self.state}, {self.country}"
        elif self.city:
            return f"{self.city}, {self.country}"
        elif self.state:
            return f"{self.state}, {self.country}"
        else:
            return self.country


class Transportation(models.Model):
    transportation_method = models.CharField(max_length=60)

    def __str__(self):
        return self.transportation_method


class Document(models.Model):
    name = models.CharField(max_length=80, help_text='Name/type of document')
    image = models.ImageField(blank=True, null=True, upload_to="account", help_text='Upload an image/screenshot of your document')
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)