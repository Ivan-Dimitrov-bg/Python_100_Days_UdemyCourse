import os
import requests

class DataManager:
# This class is responsible for talking to the Google Sheet.
    url_get = os.environ["url_get_sh"]
    url_post_sh_users = os.environ["url_post_sh_users"]
    token_sh = os.environ["token_sh"]
    print(url_post_sh_users)

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

    def update_destination_codes(self, city_name):
        for city in self.destination_data:
            if city["city"] == city_name:
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

    def save_user(self, first_name, last_name, email):

        headers_params = {
            "Authorization": f"Bearer {self.token_sh}",
            "Content-Type": "application/json",

        }

        body = {
            "user": {
                'first': first_name,
                'last': last_name,
                'email': email
            }
        }
        response = requests.post(
            url=f'{self.url_post_sh_users}',
            headers=headers_params,
            json=body)

        print(response.text)

dataManager = DataManager()

dataManager.save_user("Ivan", "Dimitrov", "Email")
