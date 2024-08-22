import requests
import pandas as pd
import json

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(url)
data = response.json()

# Create a list of the players names, their teams and prices
player_info = [[f"{player['web_name']}", f"{player['transfers_in']}", f"{player['transfers_out']}"] for player in data['elements']]

print(player_info[:5])

# Create the dataframe of the players and their transfers for the current week.
