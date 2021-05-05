import requests
import os
from flight_data import FlightData

from datetime import timedelta, datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["tequila_key"]

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    # def __init__(self, price, departure_airport_code, departure_city):
    #     self.price = price
    #     self.departure_airport_code = departure_airport_code
    #     self.departure_city = departure_city
    # https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021

    def find_the_best_price(self, origin_city_code, destination_city_code, from_time, to_time):

        search_endpoind = f"{TEQUILA_ENDPOINT}/v2/search?"
        headers = {"apikey": TEQUILA_API_KEY}
        params={
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": from_time,
            "dateTo": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        data = requests.get(url=search_endpoind, params=params, headers=headers)

        try:
            data = data.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0])

        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
