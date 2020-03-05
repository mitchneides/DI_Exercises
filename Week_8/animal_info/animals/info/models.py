from django.db import models


class Animal(models.Model):
    legs = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    speed = models.IntegerField(default=0)
    family = models.ForeignKey('Family', on_delete=models.CASCADE)


class Family(models.Model):
    name = models.TextField(max_length=60)
