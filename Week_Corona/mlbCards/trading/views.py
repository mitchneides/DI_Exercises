from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OfferModelForm
from django.db.models import Q



def index(request):
    players = Player.objects.filter(on_trade_block=True).order_by('full_name').all()
    context = {'players': players}
    return render(request, 'trading/index.html', context=context)


def all_players(request):
    players = Player.objects.order_by('full_name').all()
    context = {'players': players}
    return render(request, 'trading/all_players.html', context=context)


def free_agents(request):
    free_agents = Player.objects.filter(team_id__isnull=True).order_by('full_name').all()
    context = {'players': free_agents}
    return render(request, 'trading/free_agents.html', context=context)


@login_required
def my_team(request):
    current_user = request.user
    user_id = current_user.id

    try:
        team = Team.objects.get(user_id=user_id)
    except:
        team = "You have not yet drafted your team."
        team_context = team
    else:
        team_context = team
        team_id = team.id

    # team name or none if not created
    context = {'team': team_context}

    # if team exists; gets info such as...
    if team != "You have not yet drafted your team.":
        # players on user's team
        players = Player.objects.filter(team_id=team_id).order_by('full_name').all()
        players_context = players

        # players on trade block from user's team
        players_on_block = Player.objects.filter(team_id=team_id, on_trade_block=True).all()
        players_on_block_ids = []
        for player in players_on_block:
            players_on_block_ids.append(player.id)

        # all trade block offers for team
        teams_block_offers = Offer.objects.filter(deciding_team=team, offer_status="P").all()

        #number of pending offers for team
        num_block_offers = len(teams_block_offers)


        context = {'team': team_context, 'players': players_context, 'num_block_offers': num_block_offers}

    return render(request, 'trading/my_team.html', context)


@login_required
def trade_offers(request):
    current_user = request.user
    user_id = current_user.id

    # user's team
    team = Team.objects.get(user_id=user_id)

    # players on trade block from user's team
    players_on_block = Player.objects.filter(team_id=team.id, on_trade_block=True).all()
    players_on_block_ids = []
    for player in players_on_block:
        players_on_block_ids.append(player.id)

    # all trade block offers for team
    teams_block_offers = Offer.objects.filter(deciding_team=team, offer_status='P').all()

    # number of pending offers for team
    num_block_offers = len(teams_block_offers)

    return render(request, 'trading/trade_offers.html', context={'trade_offers': teams_block_offers, 'team': team, 'num_block_offers': num_block_offers})


@login_required
def quick_sell(request, player_id):
    current_user = request.user
    user_id = current_user.id

    # return player to free agents and remove if on trade block
    player = Player.objects.get(id=player_id)
    player.team_id = None

    if player.on_trade_block:
        player.on_trade_block = False

    player.save()
    price = player.price

    # add money to team funds
    team = Team.objects.get(user_id=user_id)
    funds = team.funds
    funds += price
    team.funds = funds
    team.save()

    messages.success(request, 'Sale complete!')

    return redirect('my_team')


@login_required
def quick_buy(request, player_id):
    current_user = request.user
    user_id = current_user.id
    user_team = Team.objects.get(user=current_user)

    player = Player.objects.get(id=player_id)

    if not player.team_id:

        cost = player.price
        user_balance = user_team.funds
        
        if user_balance >= cost:
        
            user_balance -= cost
            user_team.funds = user_balance
            user_team.save()

            player.team_id = user_team
            player.save()
    
            messages.success(request, 'Successful purchase!')
        
        else:
            
            messages.error(request, 'Denied - You do not have enough funds to make this purchase.')

        return redirect('my_team')



@login_required
def trade_block(request, player_id):
    current_user = request.user
    user_id = current_user.id

    # add player to trade block
    player = Player.objects.get(id=player_id)
    player.on_trade_block = True
    player.save()

    messages.success(request, 'Player added to trade block!')

    return redirect('index')


@login_required
def make_offer(request, player_id):
    current_user = request.user

    # get current user's players
    team = Team.objects.get(user=current_user)
    user_players = Player.objects.filter(team=team).order_by('full_name').all()

    if request.method == 'POST':
        # get form
        form = OfferModelForm(request.POST)

        if form.is_valid():
            
            offering_team_funds = team.funds

            if form.cleaned_data['money_amount'] <= offering_team_funds:

                # player info
                trade_player = Player.objects.get(id=player_id)
                current_team = trade_player.team

                # update offers in db ///NOT NECESSARY? ////////////////////////////////////
                num_offers = current_team.in_offers
                num_offers += 1
                current_team.in_offers = num_offers
                current_team.save()

                # send data from form to db
                offer = form.save(commit=False)
                offer.requesting_team = team
                offer.trade_block_player = trade_player
                offer.deciding_team = current_team
                offer.save()
                # need to save and then manually extract data for many to many field:
                for player in form.cleaned_data['offering_players']:
                    print(player)
                    offer.offering_players.add(player)

                messages.success(request, 'Offer submitted!')
                return redirect('index')

            else:

                messages.error(request, 'You do not have enough funds to make this offer - try again.')
                form = OfferModelForm()
                # update choices according to users players
                form.fields['offering_players'].choices = [(user_player.id, user_player.full_name) for user_player in user_players]

    else:
        form = OfferModelForm()
        # update choices according to users players
        form.fields['offering_players'].choices = [(user_player.id, user_player.full_name) for user_player in user_players]

    return render(request, 'trading/make_offer.html', {'form': form})


@login_required
def answer_offer(request, status, offer_id):
    current_user = request.user

    # get offer
    offer = Offer.objects.get(pk=offer_id)

    if status == 'accept':

        money = offer.money_amount
        new_team = offer.requesting_team

        if new_team.funds >= money:


            # update offer in db
            offer.offer_status = 'A'
            offer.save()

            # money updates for both teams
            money = offer.money_amount
            old_team = offer.deciding_team
            old_team.funds += money
            old_team.save()
            new_team = offer.requesting_team
            new_team.funds -= money
            new_team.save()

            # roster/trade block updates for trade_block player
            player = offer.trade_block_player
            player.team_id = new_team.id
            player.on_trade_block = False
            player.save()

            # roster updates for offered player(s)
            players = offer.offering_players.all()
            for instance_player in players:
                instance_player.team = old_team
                instance_player.save()

            # decline other offers with trade block player

            pending_offers_with_this_player = Offer.objects.filter(trade_block_player=player).all()
            for other_offer in pending_offers_with_this_player:
                ############################not working ###################################################
                print(f"OFFER S: {other_offer.offer_status}")
                ############################not returning all offers in db and none are pending###################################################
                if other_offer.offer_status == 'P':
                    other_offer.offer_status = 'R'
                    print(f"OFFER S: {other_offer.offer_status}")
                    other_offer.save()

            messages.success(request, 'Offer accepted!')

            return redirect('my_team')

        else:

            messages.error(request, f'Check from {new_team.name} bounced - they no longer have sufficient funds for this transaction.')
            offer.offer_status = 'R'
            offer.save()

            return redirect('trade_offers')

    elif status == 'decline':
        # update offer in db
        offer.offer_status = 'R'
        offer.save()

        messages.error(request, 'Offer declined!')

        return redirect('trade_offers')

    else:
        return render(request, 'trading/trade_offers.html')


def rankings(request):
    all_teams = Team.objects.all()

    team_scores = []

    for team in all_teams:
        worth = team.funds
        players_on_team = Player.objects.filter(team=team).all()
        for player in players_on_team:
            worth += player.price
            worth += (player.rbis * 2.5)
            worth += (player.runs / player.ab * 100)

        worth = round(worth)
        team_scores.append({'team': team, 'worth': worth})

    rankings = sorted(team_scores, key = lambda i: i['worth'],reverse=True)

    return render(request, 'trading/rankings.html', context={'rankings': rankings})







