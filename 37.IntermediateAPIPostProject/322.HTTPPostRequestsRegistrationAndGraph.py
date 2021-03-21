import requests
import os

# requests.get()
# requests.post()
# requests.put()
# requests.delete()


pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = os.environ["user_pixela"]
pixela_token = os.environ["token_pixela"]

# registration
# user_params = {
#     "token": pixela_token,
#     "username": pixela_username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

params_headers={
    "X-USER-TOKEN" : pixela_token
}

params_graph={
    "id" : "graph1",
    "name" : "Read English Chalange",
    "unit" : "pages",
    "type" : "int",
    "color" : "sora"

}
request = requests.post(url=graph_endpoint, json=params_graph, headers=params_headers)
print(request.text)