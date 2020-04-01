from django.shortcuts import render, redirect, reverse
from .forms import *
from account.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from account.models import *
import plotly.graph_objects as go
import datetime
from dateutil import parser


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

    # matplotly (old):
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
    purchases = Purchase.objects.filter(trip=trip) # = trip.purchase_set.all()

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

    # spending pie chart:
    labels = categories
    values = amt_spent

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial'
                                 )])
    fig.show()


    # time series graph:

    # get only relevant days of trip
    purchases_by_day = []
    for purchase in purchases:
        date_str = str(purchase.datetime).split(' ')[0]
        if date_str not in purchases_by_day:
            purchases_by_day.append(date_str)

    # convert back to datetime and sort
    purchase_dates = []
    for date in purchases_by_day:
        date_dt = parser.parse(date)
        purchase_dates.append(date_dt)

    purchase_dates.sort()

    start_date = purchase_dates[0]
    end_date = purchase_dates[-1]
    delta = datetime.timedelta(days=1)

    # get all dates in range
    date_span = []
    while start_date <= end_date:
        date_span.append(start_date.date())
        start_date += delta


    spending_by_cat_and_day = {}
    categories = set([purchase.category for purchase in purchases])

    go_bars = []

    for cat in categories:
        a = go.Bar(name=cat.name, x=date_span, y=[sum([purchase.price for purchase in purchases.filter(category=cat, datetime__contains=date)]) for date in date_span])
        go_bars.append(a)

    fig = go.Figure(data=go_bars)

    fig.update_layout(barmode='stack')

    fig.show()





















    # # {date: {cat1: 0, cat2: 0},}
    # spending_by_day_and_cat = {}
    # for date in date_span:
    #     spending_by_day_and_cat[date] = {}
    #     for purchase in purchases:
    #         spending_by_day_and_cat[date][purchase.category.name] = {'total_spent': 0}
    #
    # # print(spending_by_day_and_cat)
    #
    # # fill values:
    # # {date: {cat1: 30, cat2: 24},}
    # for purchase in purchases:
    #     # convert date to proper format
    #     date_str = str(purchase.datetime).split(' ')[0]
    #     date_dt = parser.parse(date_str)
    #     date = []
    #     date.append(date_dt)
    #
    #     spending_by_day_and_cat[date[0]][purchase.category.name]['total_spent'] += purchase.price
    #
    # print(spending_by_day_and_cat)
    #
    # for key, value in spending_by_day_and_cat:
    #
    #
    #
    # # graph
    # x = []
    # for key in spending_by_day_and_cat.keys():
    #     x.append(key.date())
    #
    # # y = []
    # # for val in spending_by_day.values():
    # #     y.append(val)
    #
    # specific_data = {}
    # for val in spending_by_day_and_cat.values():
    #     print(val)
    #
    #     for key in val.keys():
    #         specific_data[key] = []
    #
    #     for key in val.keys():
    #         specific_data[key].append(val[key]['total_spent'])
    #
    #         # specific_data.append(f"go.Bar(name={key}, x=x, y={val[key]['total_spent']})")
    #
    #
    # print(specific_data)



    # specific_data_str = ', '.join(specific_data)
    #
    #
    # fig = go.Figure(data=f"[{specific_data_str}]")
    # # Change the bar mode
    # fig.update_layout(barmode='stack')
    # fig.show()










    # for date in date_span:
    #     spending_by_day[date] = {''}
    #
    # for purchase in purchases:
    #     date_str = str(purchase.datetime).split(' ')[0]
    #     date_dt = parser.parse(date_str)
    #     spending_by_day[date_dt] += purchase.price





    # # graph
    # x = []
    # for key in spending_by_day.keys():
    #     x.append(key.date())
    #
    # y = []
    # for val in spending_by_day.values():
    #     y.append(val)
    #
    # fig = go.Figure(data=[
    #     go.Bar(name='Day', x=x, y=y),
    #     go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
    # ])
    # # Change the bar mode
    # fig.update_layout(barmode='stack')
    # fig.show()



    # line grpah
    # x = []
    # for key in spending_by_day.keys():
    #     x.append(key.date())
    #
    # y = []
    # for val in spending_by_day.values():
    #     y.append(val)
    #
    # fig = go.Figure(data=[go.Scatter(x=x, y=y)])
    # # Use datetime objects to set xaxis range
    # fig.update_layout(xaxis_range=[x[0], x[-1]], title_text='Trip Expenses by Day', yaxis_title='Money spent ($)', xaxis_rangeslider_visible=True)
    #
    # fig.show()

    return redirect('finances', trip_id)


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

