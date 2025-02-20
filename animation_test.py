import os
import time


def Cadr(x):
    if x == "q":
        print("")
    if x == "w":
        print("*")
    if x == "e":
        print("**")
    if x == "r":
        print("***")


alf = "qwer"
for _ in range(100):
    for i in alf:
        Cadr(i)
        time.sleep(0.5)
        os.system("cls")


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


import requests
import os


key = "7672D4117ED526FE041116FB7B7C28D3"
# запросы без appid
method_GetFrendList = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"
method_GetOwnedGames = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
method_GetRecentlyPlayedGames = (
    "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/"
)
# запросы с appid
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

# steam_id = input()

params = {"key": {key}, "steamid": "76561199171932413"}

response_GetFriendList = requests.get(method_GetFrendList, params=params)
print(response_GetFriendList.json())
