# application program interface
# end point - URL form where we are making the request
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
response.raise_for_status()

data = response.json()
print(data)

data_tuple = (response.json()["iss_position"]["longitude"], response.json()["iss_position"]["latitude"])
print(data_tuple)






#
# 1xx - hold On
# 2xx - Here you go
# 3xx - Go Away
# 4xx - You screwed up doesnt exist
# 5xx - server is down

