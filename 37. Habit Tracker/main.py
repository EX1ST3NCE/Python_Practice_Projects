import requests
from datetime import date, datetime

USERNAME = "ex1stence"
TOKEN = "hefiujherguihroigherkagnlk"
GRAPH_ID = "graph1"
TODAY = date.today().strftime('%Y%m%d')
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

# Params for creating a new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Params for creating a graph
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

# Params for creating a new pixel
pixel_params = {
    "date": TODAY,
    "quantity": "6.0",
}

# Params for updating pixels
pixel_update_params = {
    "quantity": "4",
}

# Request header
headers = {
    "X-USER-TOKEN": TOKEN,
}

# Response from Pixela API after creating an user
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

# Response from Pixela API after creating a graph
graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
print(graph_response.text)

# Response from API after creating a pixel
pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(pixel_response.text)

# Response from API after updating a pixel
update_response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_params, headers=headers)
print(update_response.text)

# Response from API after deleting a pixel
delete_response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
print(delete_response.text)