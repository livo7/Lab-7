import json
import requests


city_name = "Moscow"
key = "23669f1de3fdef18a478b8fad43d9be7"
response = requests.post(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}"
)
result = json.loads(response.text)
weather_list = result["weather"]
weather = weather_list[0]
main_weather = weather["main"]
main = result["main"]
pressure = main["pressure"]
humidity = main["humidity"]

print(f"погода - {main_weather}, давление - {pressure}, влажность - {humidity}")
