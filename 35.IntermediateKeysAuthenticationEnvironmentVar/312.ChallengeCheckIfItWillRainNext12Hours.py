import requests

MY_LAT = 42.697708 # Your latitude
MY_LONG = 23.321867 # Your longitude
(43.121980, 25.689490)
MY_KEY = "86a837cb94ab6bec7e6ceaf174329d51"
params={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "exclude": "current,minutely,daily",
    "appid":MY_KEY
}


data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
data.raise_for_status()
data_weather = data.json()


it_will_rain = False
rain_hour = 0
for h in range(0,12):
    wether_next_12H = data.json()["hourly"][h]["weather"][0]["id"]
    print(data.json()["hourly"][h]["weather"][0].values())
    if wether_next_12H < 700:
        it_will_rain = True
        rain_hour = h

if it_will_rain:
    print("Bring an umbrella.")