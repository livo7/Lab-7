import requests
import json
import os


key = "7672D4117ED526FE041116FB7B7C28D3"
main_url_request = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"

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

method_GetFrendList = "ISteamUserStats/GetPlayerAchievements/v0001/"
method_GetOwnedGames = "IPlayerService/GetOwnedGames/v0001/"
method_GetRecentlyPlayedGames = "IPlayerService/GetRecentlyPlayedGames/v0001/"
params = {"key": {key}, "steamid": {steam_id}}

response_GetFriendList = requests.get(url=main_url_request, params=params)
# response_GetOwnedGames = requests.get(f"{main_url_request}{method_GetOwnedGames}", params=params)
# response_GetRecentlyPlayedGames = requests.get(f"{main_url_request}{method_GetRecentlyPlayedGames}", params=params)

# result_GetFriendList = json.loads(response_GetFriendList.text)
# result_GetOwnedGames = response_GetOwnedGames.json()
# result_GetRecentlyPlayedGames = response_GetRecentlyPlayedGames.json()

print(response_GetFriendList.json)


# Interfaces or method
# >>>GetFriendList (v0001)
# >>>GetOwnedGames (v0001)
# >>>GetRecentlyPlayedGames (v0001)

# >>>GetPlayerAchievements (v0001)
# >>>GetUserStatsForGame (v0002)


# method_GetUserStatsForGame = "ISteamUserStats/GetUserStatsForGame/v0002/"
# method_GetPlayerAchievements = "ISteamUserStats/GetPlayerAchievements/v0001/"

# response_GetUserStatsForGame = requests.get(f"{main_url_request}{method_GetUserStatsForGame}")
# response_GetPlayerAchievements = requests.get(f"{main_url_request}{method_GetPlayerAchievements}")

# print(
#     """Введиде ID игры:
#     *Примеры ID игр
#     >>>Terraria - 1050600
#     >>>Apex Legends - 1172470
#     >>>Subnautica - 264710
#     >>>Subnautica: Below Zero - 848450
#     >>>The Elder Scrolls V: Skyrim - 489830
#     >>>NieR:Automata™ - 524220
#     >>>Satisfactory - 526870

#     ID игры можно получить из url игры в магазине игр steam, к примеру у игры "terraria"
#     url - "https://store.steampowered.com/app/105600/Terraria/" => ID - "1050600" """
# )
#
# app_id = input()
