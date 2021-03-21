import requests
import os

pixela_endpoint = "https://pixe.la/v1/users/"
pixela_username = os.environ["user_pixela"]
pixela_token = os.environ["token_pixela"]
pixela_graphID = "graph1"
date_to_be_updated = '20210321'

headers_json = {
    "X-USER-TOKEN":pixela_token
}

params_json ={
    "quantity":5,
}
url_end_point_put =  f"{pixela_endpoint}{pixela_username}/graphs/{pixela_graphID}/{date_to_be_updated}"
data = requests.post(url=url_end_point_put, json=params_json, headers=headers_json)
print(data.text)

delete_endpoint=f"{pixela_endpoint}{pixela_username}/graphs/{pixela_graphID}/{date_to_be_updated}"
data = requests.delete(url=url_end_point_put, json=params_json, headers=headers_json)
print(data.text)