from twilio.rest import Client
import requests
import os

LAT_LONG = (42.337158, 23.557369)
MY_LAT = LAT_LONG[0] # Your latitude
MY_LONG = LAT_LONG[1] # Your longitude

MY_KEY = os.environ["key_weather"]

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=" ",
        from_=os.environ["Tel_Send"],
        to=os.environ["Tel_Mine"],
    )
    print(message.status)