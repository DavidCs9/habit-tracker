import requests
from _datetime import datetime

USERNAME = "davidcs"
TOKEN = "dshadhasdkjhasjkldh"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Reading Graph",
#     "unit": "minutes",
#     "type": "int",
#     "color": "sora"
# }
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
user_input = int(input("Cuantos minutos leiste hoy? "))
today = datetime.now()
post_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": user_input
}


response = requests.post(url=post_value_endpoint, json=post_config, headers=headers)
print(response.text)