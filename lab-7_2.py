from pickle import APPEND
import requests
import json
import os

key = "7672D4117ED526FE041116FB7B7C28D3"
# with out appid
method_GetFrendList = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"
method_GetOwnedGames = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
method_GetRecentlyPlayedGames = (
    "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/"
)
# with appid
method_GetUserStatsForGame = (
    "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"
)
method_GetPlayerAchievements = (
    "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"
)


print(
    """Вы можете узнать о пользователе:
    1)Список друзей пользователя; 
    2)Все достижения пользователя в игре; 
    3)Узнать какими играми владеет пользователь; 
    4)Узнать статус пользователя; 
    5)Узнать в недавно запущиные игры пользователя;"""
)

print(
    """Введиде SteamID пользователя:
      *Пример SteamID - 76561199171932413"""
)
steam_id = input()

params = {"key": {key}, "steamid": {steam_id}, "appid": ""}

response_GetFrendList = requests.get(method_GetFrendList, params=params)
result_GetFrendList = response_GetFrendList.json()
friendslist = result_GetFrendList["friendslist"]
friends = friendslist["friends"]
print(f"Список друзей пользователя {steam_id}:")

for _ in range(len(friends)):
    # friend.append(friends[_]["steamid"])
    method_GetFrendName = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {"key": {key}, "steamids": {friends[_]["steamid"]}}
    response_GetFrendName = requests.get(method_GetFrendName, params=params)
    result_GetFrendName = response_GetFrendName.json()
    print(
        f"{_ + 1}) имя друга:{result_GetFrendName['response']['players'][0]['personaname']}, steamID друга :{friends[_]['steamid']}"
    )
