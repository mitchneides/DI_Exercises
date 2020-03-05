from django.db import models
from phone_field import PhoneField


class Customer(models.Model):
    name = models.TextField(max_length=60)
    email = models.TextField(max_length=60)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.TextField(max_length=60)
    city = models.TextField(max_length=60)
    country = models.TextField(max_length=60)


class VehicleType(models.Model):
    type = models.TextField(max_length=60)


class VehicleSize(models.Model):
    size = models.TextField(max_length=60)


class Vehicle(models.Model):
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=False, auto_now_add=False)
    real_cost = models.FloatField()
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class Rental(models.Model):
    rental_date = models.DateField(auto_now=False, auto_now_add=False)
    return_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Rent Date: {self.rental_date}>'


class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)




