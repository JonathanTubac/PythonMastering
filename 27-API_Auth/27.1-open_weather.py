import requests as r

params = {
    "lat": 14.586791,
    "lon": -90.527897,
    #now we need to authenticate our get request
    "appid": "your_api_key"
}
response = r.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

print(data)