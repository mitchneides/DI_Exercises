from django.db import models
from django.conf import settings
from account.models import *
from django.utils import timezone


class Purchase(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=200, help_text="Amount/size/description/etc", null=True, blank=True)
    category =  models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    datetime = models.DateTimeField(default=timezone.now)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name="made_purchase")
    sharers = models.ManyToManyField(Profile, related_name="splitting_purchase")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, related_name="which_budget")

    def __str__(self):
        return f"{self.item}: ${self.price}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



