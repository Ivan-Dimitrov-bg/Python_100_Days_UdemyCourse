import requests
import os
from datetime import datetime

url_pixela_endpoint = "https://pixe.la/v1/users/"
pixela_username = os.environ["user_pixela"]
pixela_token = os.environ["token_pixela"]
graphID = "graph1"

date = datetime.today().strftime("%Y%m%d")
date = "20200319"
print(date)
quantity = "10"
additional_information ={
    "Book": "Homodeus"
}

headers_json = {
    "X-USER-TOKEN" : pixela_token
}

params_json ={
    "date" : date,
    "quantity" : quantity,
}
url_pixela_endpoint_pixels = f"{url_pixela_endpoint}{pixela_username}/graphs/{graphID}"
print(url_pixela_endpoint_pixels)

data = requests.post(url=url_pixela_endpoint_pixels, json=params_json, headers=headers_json)
print(data.text)
