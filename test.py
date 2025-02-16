import requests
import os
import time

key = "7672D4117ED526FE041116FB7B7C28D3"
url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"
params = {
    "key": {key},
    "steamid": "76561199171932413",
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()  # Проверка на ошибки HTTP
    print(response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
