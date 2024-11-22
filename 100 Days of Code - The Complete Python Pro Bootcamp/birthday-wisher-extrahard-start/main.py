import random
from email.mime.text import MIMEText

import pandas
import datetime as dt
import smtplib


my_email = "my@gmail.com"
password = "abcdefg"
smtp_server = "smtp.gmail.com"

##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv('birthdays.csv')
birth_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}

if today in birth_dict:
    letter_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter_path) as letter_file:
        letters = letter_file.read()
        birth_person = birth_dict[today]
        new_letter = letters.replace("[NAME]", birth_person["name"])
        subject = "Happy Birthday"
        body = new_letter
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = my_email
        msg["To"] = birth_person["email"]

        with smtplib.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(my_email, msg["To"], msg.as_string())
