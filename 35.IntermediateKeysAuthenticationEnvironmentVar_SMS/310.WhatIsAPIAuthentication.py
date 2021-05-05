import requests
import os

MY_LAT = 42.697708 # Your latitude
MY_LONG = 23.321867 # Your longitude
# (43.121980, 25.689490)
MY_KEY = os.environ["key_weather"]
params={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":MY_KEY
}


data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
data.raise_for_status()
print(data.json())