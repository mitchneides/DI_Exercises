from django.shortcuts import render, redirect, reverse
from .forms import *
from account.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from account.models import *
# import matplotlib
# matplotlib.use('Agg')
from matplotlib import pyplot as plt


@login_required
def index(request):
    current_user = request.user
    user_trips = Trip.objects.filter(travelers__user=current_user)

    context = {'user': current_user, 'trips': user_trips}
    return render(request, 'spending/index.html', context)


@login_required
def finances(request, trip_id):
    current_user = request.user
    trip = Trip.objects.get(id=trip_id)
    purchases = Purchase.objects.filter(trip=trip)

    trip_members = trip.travelers.all()

    everyone_purchasing_records = {}
    for person in trip_members:
        everyone_purchasing_records[person] = {}

        total_person_payments = 0
        total_person_debts = 0

        for purchase in purchases:
            sharers = purchase.sharers.all()

            # sum total money that person has paid for
            if purchase.buyer == person:
                total_person_payments += purchase.price

            # sum total share of expenses that user is responsible for
            if person in sharers:
                cost_per_sharer = (purchase.price / len(sharers))
                total_person_debts += cost_per_sharer

        everyone_purchasing_records[person]['total_paid'] = total_person_payments
        everyone_purchasing_records[person]['total_debts'] = total_person_debts
        balance = total_person_payments - total_person_debts
        if balance >= 0:
            everyone_purchasing_records[person]['to_pay'] = 0
            everyone_purchasing_records[person]['to_receive'] = balance
        else:
            everyone_purchasing_records[person]['to_pay'] = balance * -1
            everyone_purchasing_records[person]['to_receive'] = 0

    # # graphing(moved to analytics, below):
    #
    # purchase_data_by_cat = {}
    #
    # # initialize all existing categories
    # for purchase in purchases:
    #     purchase_data_by_cat[purchase.category] = {'num_purchases': 0, 'total_spent': 0}
    #
    # # count number of occurances/amount spend for each category
    # for purchase in purchases:
    #     purchase_data_by_cat[purchase.category]['num_purchases'] += 1
    #     purchase_data_by_cat[purchase.category]['total_spent'] += purchase.price
    #
    #
    # categories = [cat.name for cat in purchase_data_by_cat]
    # amt_spent = [purchase_data_by_cat[cat]['total_spent'] for cat in purchase_data_by_cat]
    #
    # fig1, ax1 = plt.subplots()
    # ax1.pie(amt_spent, labels=categories, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #
    # plt.show()


    context = {'trip': trip, 'purchases': purchases, 'records': everyone_purchasing_records}
    return render(request, 'spending/trip_finances.html', context)


@login_required
def analytics(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    purchases = Purchase.objects.filter(trip=trip)

    purchase_data_by_cat = {}

    # initialize all existing categories
    for purchase in purchases:
        purchase_data_by_cat[purchase.category] = {'num_purchases': 0, 'total_spent': 0}

    # count number of occurances/amount spend for each category
    for purchase in purchases:
        purchase_data_by_cat[purchase.category]['num_purchases'] += 1
        purchase_data_by_cat[purchase.category]['total_spent'] += purchase.price

    # graphing:

    categories = [cat.name for cat in purchase_data_by_cat]
    amt_spent = [purchase_data_by_cat[cat]['total_spent'] for cat in purchase_data_by_cat]

    fig1, ax1 = plt.subplots()
    ax1.pie(amt_spent, labels=categories, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

    return redirect('finances', trip_id)

    # django graphing (not working):

    # xdata = categories
    # ydata = amt_spent
    #
    # extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    # chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    # charttype = "pieChart"
    #
    # data = {
    #     'charttype': charttype,
    #     'chartdata': chartdata,
    # }

    # return render(request, 'spending/analytics.html', context=data)


@login_required
def add_purchase(request, trip_id):

    if request.method == 'POST':
        form = PurchaseModelForm(request.POST)

        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()

            for sharer in form.cleaned_data['sharers']:
                purchase.sharers.add(sharer)

            messages.success(request, "Purchase added!")
            return redirect('finances', trip_id)

    else:
        form = PurchaseModelForm()


    return render(request, 'spending/add_purchase.html', {'form': form})


@login_required
def edit_purchase(request, item_id, trip_id):
    item = Purchase.objects.get(id=item_id)

    if request.method == 'POST':
        form = PurchaseModelForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.save()

            for sharer in form.cleaned_data['sharers']:
                purchase.sharers.add(sharer)

            messages.success(request, "Purchase updated!")
            return redirect('finances', trip_id)

    else:
        form = PurchaseModelForm(instance=item)


    return render(request, 'spending/edit_purchase.html', {'form': form})


@login_required
def delete_purchase(request, item_id, trip_id):
    purchase = Purchase.objects.get(id=item_id)

    purchase.delete()
    messages.success(request, "Purchase deleted")

    return redirect('finances', trip_id)

