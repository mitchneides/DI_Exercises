from django.shortcuts import render
from rent.models import Rental, Customer, Vehicle, VehicleType
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, template_name='rent/index.html')


def customer(request):
    return render(request, template_name='rent/customer.html')


def vehicle(request):
    return render(request, template_name='rent/vehicle.html')


@login_required
def rental(request):
    rental_data = Rental.objects.all().order_by('-return_date')

    return render(request, template_name='rent/rental.html', context={'rentals': rental_data})