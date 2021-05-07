import os
import requests
from email_data import EmailData

class DataManager:

    url_sh_price = os.environ["url_sh_price"]
    url_sh_users = os.environ["url_sh_users"]
    token_sh = os.environ["token_sh"]

    def __init__(self):
        self.destination_data = {}
        self.emails_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        headers_params = {
            "Authorization": f"Bearer {self.token_sh}",
            "Content-Type": "application/json",
        }

        response = requests.get(url=self.url_sh_price, headers=headers_params)
        data = response.json()
        self.destination_data = data["prices"]
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
                    url=f"{self.url_sh_price}/{city['id']}",
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
            url=f'{self.url_sh_users}',
            headers=headers_params,
            json=body)

        print(response.text)

    def get_mails(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        headers_params = {
        "Authorization": f"Bearer {self.token_sh}",
        "Content-Type": "application/json",
        }

        response = requests.get(url=self.url_sh_users, headers=headers_params)
        data = response.json()

        self.emails_data = data['users']

        return self.emails_data


# dataManager = DataManager()
# dataManager.save_user("Ivan", "Dimitrov", "Email")
dataManager = DataManager()
dataManager.get_mails()