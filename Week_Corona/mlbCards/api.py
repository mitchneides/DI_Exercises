import os
import django
import requests


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlbCards.settings')
django.setup()

from trading.models import Player



def get_top_150():
    for i in range(0, 150):
        # get full_name
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['name_display_first_last']
        full_name = response

        # get position
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['pos']
        position = response

        # get rank
        #     get price from rank
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['rank']
        rank = response

        numbers = {1: 4, 4: 11, 11: 21, 21: 31, 31: 41, 51: 61, 61: 71, 71: 81, 81: 101, 101: 116, 116: 150}
        pricing = {4: 500, 11: 450, 21: 400, 31: 350, 41: 300, 51: 250, 61: 200, 71: 150, 81: 100, 101: 75, 116:50, 151: 25}
        for key, value in numbers.items():
            if key <= int(rank) < value:
                price = pricing[value]

        # get batting_avg
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['avg']
        batting_avg = response

        # get slg
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['slg']
        slg = response

        # get homeruns
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['hr']
        homeruns = response

        # get rbis
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['rbi']
        rbis = response

        # get obp
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['obp']
        obp = response

        # get runs
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['r']
        runs = response

        # get ab
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['ab']
        ab = response

        # get api_id
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['player_id']
        api_id = response

        # get batting_hand
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['bats']
        batting_hand = response

        # get mlb_team
        response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=150&game_type='R'&season='2019'&sort_column='avg'")
        response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][i]['team_name']
        mlb_team = response

        print(i)
        player = Player(full_name=full_name, position=position, rank=rank, batting_avg=batting_avg, slg=slg, homeruns=homeruns, rbis=rbis, obp=obp, runs=runs, ab=ab, api_id=api_id, batting_hand=batting_hand, mlb_team=mlb_team, price=price)
        player.save()


get_top_150()






# def get_all_team_ids():
#     team_ids = []
#     for i in range(i,29):
#         response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&sort_order=name_asc&season='2019'")
#         response = response.json()['team_all_season']['queryResults']['row'][i]['mlb_org_id']
#         team_ids.append(response)
#     print(team_ids)
#     return team_ids
#
#
# team_id_list = get_all_team_ids()
#
#
# def get_all_player_ids_on_team(team_ids):
#     all_player_ids = []
#     for team in team_ids:
#         for i in range(0, 40):
#             response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season='2018'&end_season='2019'&team_id={team}")
#             response = response.json()['roster_team_alltime']['queryResults']['row'][i]['player_id']
#             all_player_ids.append(response)
#     print(all_player_ids)
#     return all_player_ids
#
#
# get_all_player_ids_on_team(team_id_list)
