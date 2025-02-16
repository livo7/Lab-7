import requests
import os
import time

key = "7672D4117ED526FE041116FB7B7C28D3"
url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
params = {"key": {key}, "steamids": "76561199171932413"}

response = requests.get(url, params=params)
print(response.json())
