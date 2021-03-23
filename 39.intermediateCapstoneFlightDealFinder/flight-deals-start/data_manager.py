import os
import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    url_get = os.environ["url_get_sh"]
    token_sh = os.environ["token_sh"]

    def __init__(self):
        self.destination_data = {}

    def get_data(self):

        headers_params = {
            "Authorization": f"Bearer {self.token_sh}",
            "Content-Type": "application/json",

        }
        print(self.url_get)
        response = requests.get(url=self.url_get, headers=headers_params)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]

    def update_destination_codes(self):
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



