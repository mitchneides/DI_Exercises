from django.db import models
from django.conf import settings
from account.models import *
from spending.models import *
from phonenumber_field.modelfields import PhoneNumberField


class DayPlan(models.Model):
    date = models.DateField(help_text='Select the day of the trip')
    name = models.CharField(max_length=200, help_text='Give a name to remember what was/will be done on this day')
    destinations = models.ManyToManyField(Destination, help_text='Ctrl + click to select multiple', blank=True)
    requirements = models.CharField(max_length=500, help_text='List anything you may need to bring', blank=True, null=True)
    contacts = models.ManyToManyField('Contact', blank=True)
    transportation_methods = models.ManyToManyField(Transportation, related_name='DayTransportation', blank=True, help_text='Ctrl + click to select multiple')
    journal = models.CharField(max_length=1000, help_text='To be completed after - write any notes/memories from this day', blank=True, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    phone_number = PhoneNumberField(blank=True, help_text="(format: +12125552368)")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.company}: {self.phone_number}"