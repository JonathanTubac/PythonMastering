import requests as req
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "mordecaa"
TOKEN = "fwafsafw"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


#response = req.post(url=f"{PIXELA_ENDPOINT}/users", json=user_params)
#print(response.text)

#Creating a graph via post http method

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#graph_response = req.post(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", headers=headers, json=graph_config)

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8.78"
}

#pixel_response = req.post(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}", json=pixel_data, headers=headers)

new_pixel_data = {
    "quantity": "45.2"
}
#update_reponse = req.put(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}", json=new_pixel_data, headers=headers)
#print(update_reponse.text)

delete_response = req.delete(f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}", headers=headers)
print(delete_response.text)
