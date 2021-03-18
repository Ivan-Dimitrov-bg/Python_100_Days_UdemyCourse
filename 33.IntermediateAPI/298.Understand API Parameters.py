import requests
from datetime import datetime

MY_LAT = 42.697708
MY_LNG = 23.321867

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

responce = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
responce.raise_for_status()
sunrise = responce.json()["results"]["sunrise"]
sunset = responce.json()["results"]["sunset"]

sunrise_h = sunrise.split("T")[1].split(":")[0]
sunset_h = sunset.split("T")[1].split(":")[0]
time_now = datetime.now().hour

print(sunrise_h)
print(sunset_h)
print(time_now)
