import requests as req
from bs4 import BeautifulSoup
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

#Constants
TARGET_PRICE = 150

#Getting enviroment variables
email = os.getenv("EMAIL")
password = os.getenv("APP_PASS")
url = os.getenv("URL")

#Setting the headers odd tthe broser, to look more human, not like a bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0",
    "Accept-Language": "es-419,es;q=0.9,en;q=0.8,id;q=0.7,pt-BR;q=0.6,pt;q=0.5"
}

#We make the request
response = req.get(url, headers=headers)

#We scrap the price in amazon page
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(class_="aok-offscreen").getText()
formatted_price = float(price.replace(",", ".").replace("€", ""))

#We validate the price and send a email
if formatted_price < TARGET_PRICE:
    with SMTP("smtp.gmail.com", 587) as con:
        con.starttls()
        con.login(email, password)
        message = f"Subject:Item price under target price!\nContent-Type: text/plain; charset=utf-8\n\nHellooo! Your item price is at {str(formatted_price)}, buy it now!\nGo get it at: {url}"
        con.sendmail(
            email,
            email,
            message.encode('utf-8')
        )
else:
    print("Your item price is higher than you want!")
