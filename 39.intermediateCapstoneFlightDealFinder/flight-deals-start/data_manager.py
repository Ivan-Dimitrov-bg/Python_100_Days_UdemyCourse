import os
import requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    url_get = os.environ["url_get_sh"]
    token_sh = os.environ["token_sh"]

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        headers_params = {
            "Authorization": f"Bearer {self.token_sh}",
            "Content-Type": "application/json",

        }
        response = requests.get(url=self.url_get, headers=headers_params)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint().
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        flight_search = FlightSearch()
        for city in self.destination_data:
            headers_params = {
                "Authorization": f"Bearer {self.token_sh}",
                "Content-Type": "application/json",

            }
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }

            }
            response = requests.put(
                url=f"{self.url_get}/{city['id']}",
                json=new_data,
                headers=headers_params,
            )
            print(response.text)
# test
# data_manager = DataManager()
# data_manager.get_data()
# data_manager.update_destination_codes()



