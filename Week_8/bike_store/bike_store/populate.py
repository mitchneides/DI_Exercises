import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import Customer
from faker import Faker

fake = Faker()

names = []
emails = []
phone_numbers = []
addresses = []
cities = []
countries = []

for x in range(10):
    names.append(fake.name())
    emails.append(fake.ascii_email())
    phone_numbers.append(fake.phone_number())
    addresses.append(fake.address())
    cities.append(fake.city())
    countries.append(fake.country())

print('Populating Customer table...')
for n, name in enumerate(names):
    c = Customer(name=names[n], email=emails[n], phone_number=phone_numbers[n], address=addresses[n], city=cities[n], country=countries[n])
    c.save()
print('Done')