from datetime import timedelta, datetime
import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["tequila_key"]

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, departure_airport_code, departure_city):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
    # https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
    def find_the_best_price(self):

        search_endpoind = f"{TEQUILA_ENDPOINT}/v2/search?"
        fly_from = "LON"
        fly_to = self.departure_airport_code
        today_day = datetime.now().strftime("%d/%m/%Y")
        date_to = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")

        headers = {"apikey": TEQUILA_API_KEY}
        params={
            "fly_from": fly_from,
            "fly_to": fly_to,
            "dateFrom": today_day,
            "dateTo": date_to
        }
        # debug!!
        # data = requests.get(url=search_endpoind, params=params, headers=headers)
        # print(data.json())






# Try to use the FlightData class to represent the flight data.
# e.g. You can create attributes for
# price,
# departure_airport_code,
# departure_city etc.