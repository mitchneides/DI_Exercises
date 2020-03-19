import requests
import json



# scores = {}
# for week in range(1, 17):
#     r = requests.get('http://games.espn.com/ffl/api/v2/scoreboard', 
#                      params={'leagueId': 123456, 'seasonId': 2017, 'matchupPeriodId': week})
#     scores[week] = r.json()

# def theattempt():
# 	count = 0
# 	attemptnum = 0
# 	for id in range(300000,400000):
# 	    response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id={id}")
	    
# 	    try:
# 	    	print(response.json()['player_info']['queryResults']['row']['name_last'])
# 	    	print(f"c: {count}")
# 	    	count += 1
# 	    except Exception as e:
# 	    	continue
# 	    finally:
# 	    	print(f"a: {attemptnum}")
# 	    	attemptnum += 1
# 	return count



# http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='young%'&search_player_all.col_in=player_id
# def attempt1():
# 	# response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season='2018'&end_season='2019'&team_id='121'")
# 	# response = response.json()['roster_team_alltime']['queryResults']['row'][10]['player_id']
# 	# print(response)

# 	for i in range(0,83):
# 		response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.roster_team_alltime.bam?start_season='2018'&end_season='2019'&team_id='121'")
# 		response = response.json()['roster_team_alltime']['queryResults']['row'][i]['player_id']
# 		print(response)
		

# 	return i


# attempt1()



def get_all_team_ids():
    team_ids = []
    response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=50&game_type='R'&season='2019'&sort_column='avg'")
    response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][0]['avg']
    print(response)
    response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=50&game_type='R'&season='2019'&sort_column='avg'")
    response = response.json()['leader_hitting_repeater']['leader_hitting_mux']['queryResults']['row'][0]['player_id']
    print(response)
    return team_ids

get_all_team_ids()



# response = requests.get(f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='293320'")
# print(response)
# response = response.json()['player_info']['queryResults']['row']['name_last']
# print(response)
# print(response['name_display_first_last'])
# print(response['status_code'])




# response = requests.get(f"https://api.nfl.com/v1/persons/32004d41-4371-0352-e57d-251eacb121bd?fs={playerStats{teamStats{passing}}}")
# print(response.json())




# from main.models import Card

# for number in range(1, 100):
# 	response = requests.get(f"https://asdfasdfasdf.com/api/players/{number}")
# 	print(response.json())
# 	info = response.json()
# 	care = Card(name=info['name'], families=info['allegiances'], spouse=info['spouse'])

# 	card.save()



# def search_player(name):
# 	name = name.replace(' ', '%20')
# 	response = requests.get()
# 	headers={

# 	}
# 	return response.json()['results']