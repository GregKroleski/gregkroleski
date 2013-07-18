import csv
import json

from collections import defaultdict

season_data = csv.reader(open('data/nflseasondata.csv', "rU"), delimiter = ",", )
team_data = csv.reader(open('data/nflteamdata.csv', "rU"), delimiter = ",")
# Skip first lines
team_data.next()
season_data.next()

team_season_list = []
team_season_data = defaultdict(dict)

for team_name, color, display_name in team_data:
    team_season_data[team_name] = defaultdict(dict)
    team_season_data[team_name]['team'] = team_name
    team_season_data[team_name]['color'] = color
    team_season_data[team_name]['display_name'] = display_name
    team_season_data[team_name]['seasons'] = []

for team_name, year, wins, losses, ties in season_data:
    season_dict = {}
    season_dict['year'] = year
    season_dict['wins'] = wins
    season_dict['losses'] = losses
    season_dict['ties'] = ties
    season_dict['record'] = (int(wins) + (.5 * int(ties))) / (int(wins) + int(ties) + int(losses))

    team_season_data[team_name]['seasons'].append(season_dict)

print team_season_data

for key, value in team_season_data.items():
    team_season_list.append(value)

f = open('data/nfl_team_season_data.json', 'w')
f.write(json.dumps(team_season_list))
