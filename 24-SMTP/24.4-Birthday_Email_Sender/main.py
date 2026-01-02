import pandas as pd
import random as r
from datetime import datetime
from smtplib import SMTP

#Constants, never changes during the execution
BIRTHDAYS_PATH = "./24-SMTP/24.4-Birthday_Email_Sender/birthdays.csv"
HOST_PROVIDER = "smtp.gmail.com"
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
PORT = 587

#This function sends the message to the destin gmail with the template
def send_email(template, destin):
    with SMTP(HOST_PROVIDER, PORT) as con:
        con.starttls()
        con.login(EMAIL, APP_PASSWORD)
        con.sendmail(EMAIL, destin, f"Subject:Happy Birthday!\n\n{template}")
        con.close()

#We create the dataframe
df = pd.read_csv(BIRTHDAYS_PATH)
#We retrieve the actual date
current_time = datetime.now()
#We divide the actual_date in a tuple
today = (current_time.month, current_time.day)

#We use dict_comprehension to create a dictionary with the data from the dataframe
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

#We validate the current date to check if it's someone birthday
if today in birthday_dict:
    random_template = r.randint(1, 3)
    template_path = f"24-SMTP/24.4-Birthday_Email_Sender/letter_templates/letter_{random_template}.txt"
    with open(template_path) as file:
        content = file.read()
        template = content.replace("[NAME]", birthday_dict[today]["name"])
    send_email(template, birthday_dict[today]["email"])
    
    

