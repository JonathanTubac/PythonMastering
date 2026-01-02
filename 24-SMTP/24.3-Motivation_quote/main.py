import smtplib as spt
import random as r
import datetime as dt

FILE_PATH = "./23-SMTP/23.3-Motivation_quote/quotes.txt"
HOST_PROVIDER = "smtp.gmail.com"
PORT = 587
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

#This function separates the lines of a file and returns a list
def readlines_of_file(path):
    file = open(path)
    content = file.readlines()
    return content

#This function returns a random quote from a list
def choose_random_quote(quotes):
    random_quote = r.choice(quotes)
    return random_quote

#This function sends a email with a quote
def send_email(quote):
    with spt.SMTP(HOST_PROVIDER, PORT) as con:
        con.starttls()
        con.login(EMAIL, APP_PASSWORD)
        con.sendmail(EMAIL, EMAIL, f"Subject: Friday Motivational Quote\n\n{quote}")
        con.close()
        
actual_time = dt.datetime.now()
quotes = readlines_of_file(FILE_PATH)
random_quote = choose_random_quote(quotes)

if actual_time.weekday() == 4:
    send_email(random_quote)
else:
    print("is not friday yet!😎")
