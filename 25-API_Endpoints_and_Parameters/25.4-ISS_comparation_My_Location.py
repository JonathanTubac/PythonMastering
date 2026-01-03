import requests as rq
from smtplib import SMTP
from datetime import datetime

#Constants
MY_POSITION = (15.783471, -90.207882)
HOST = "smtp.gmail.com"
EMAIL = "your_email@gmail.com"
APP_PASS = "your_app_password"

#We get the position of iss with a get request
def get_iss_location():
    response = rq.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    return (float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"]))

#we get info about the time in our position
def get_time_info(params):
    response = rq.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    return data["results"]

#We validate if it's night
def is_night(actual_time, sunset_hour, sunrise_hour):
    if actual_time >= sunset_hour or actual_hour <= sunrise_hour:
        return True
    else:
        return False
    
#We validate if iss is near from our position
def is_iss_near(my_position, iss_position):
    if my_position[0] - 5 <= iss_position[0] <= my_position[0] + 5 and my_position[1] - 5 <= iss_position[1] <= my_position[1] + 5:
        return True
    else:
        return False

#We send an email   
def send_email():
    with SMTP(HOST, 587) as con:
        con.starttls()
        con.login(EMAIL, APP_PASS)
        con.sendmail(EMAIL, EMAIL, "Subject:Wake UP!\n\nLook the sky! The ISS is near from your location")
        con.close()
   


iss_position = get_iss_location()
actual_hour = datetime.now().hour
params = {
    "lat": MY_POSITION[0],
    "lng": MY_POSITION[1],
    "formatted": 0
}
time_info = get_time_info(params)
sunset_hour = int(time_info["sunset"].split("T")[1].split(":")[0])
sunrise_hour = int(time_info["sunrise"].split("T")[1].split(":")[0])

#If it's night and the iss is near from you, an email will be sent to you
if is_iss_near(MY_POSITION, iss_position) and is_night(actual_hour, sunset_hour, sunrise_hour):
    send_email()
else:
    print("not night or not near")
