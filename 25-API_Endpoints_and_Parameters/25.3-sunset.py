import requests as rq
from datetime import datetime

params = {
    "lat": 23,
    "lng": 50,
    "formatted": 0
}

response = rq.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
sunrise_hour = sunrise.split("T")[1].split(":")[0]
print(sunrise_hour)
actual_hour = datetime.now().hour
print(actual_hour)

