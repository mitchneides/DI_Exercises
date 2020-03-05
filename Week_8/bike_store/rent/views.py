from django.shortcuts import render
from rent.models import Rental, Customer, Vehicle


def index(request):
    return render(request, template_name='rent/index.html')


def customer(request):
    return render(request, template_name='rent/customer.html')


def vehicle(request):
    return render(request, template_name='rent/vehicle.html')


def rental(request):
    rental_data = Rental.objects.all().order_by('-return_date')
    
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
# need to get the type of the vehicle, not just the object ////////////////////////////
    # party = Party.objects.get(pk=pk)

    return render(request, template_name='rent/rental.html', context={'rentals': rental_data, 'customers': customers, 'vehicles': vehicles})