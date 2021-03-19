import requests

MY_LAT = 42.697708 # Your latitude
MY_LONG = 23.321867 # Your longitude
(43.121980, 25.689490)
MY_KEY = "86a837cb94ab6bec7e6ceaf174329d51"
params={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":MY_KEY
}


data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
data.raise_for_status()
print(data.json())