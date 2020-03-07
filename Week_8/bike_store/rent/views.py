from django.shortcuts import render
from rent.models import Rental, Customer, Vehicle, VehicleType


def index(request):
    return render(request, template_name='rent/index.html')


def customer(request):
    return render(request, template_name='rent/customer.html')


def vehicle(request):
    return render(request, template_name='rent/vehicle.html')


def rental(request):
    rental_data = Rental.objects.all().order_by('-return_date')

    vehicle_ids = []
    customer_ids = []
    for c,item in enumerate(rental_data):
        vehicle_ids.append(Rental.objects.get(pk=c+1).vehicle_id)
        customer_ids.append(Rental.objects.get(pk=c+1).customer_id)

    vehicle_names = []
    for item in vehicle_ids:
        print(item)
        vehicle_names.append(VehicleType.objects.get(pk=item).type)

    customer_names = []
    for item in customer_ids:
        customer_names.append(Customer.objects.get(pk=item).name)


    return render(request, template_name='rent/rental.html', context={'rentals': rental_data, 'customers': customer_names, 'vehicles': vehicle_names})