import random
from email.mime.text import MIMEText

import pandas
import datetime as dt
import smtplib


##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

with open("./letter_templates/letter_1.txt") as letter1:
    letter1_list = letter1.read()
with open("./letter_templates/letter_1.txt") as letter2:
    letter2_list = letter2.read()
with open("./letter_templates/letter_1.txt") as letter3:
    letter3_list = letter3.read()
letter_list = [letter1_list, letter2_list, letter3_list]

letters = random.choice(letter_list)

my_email = "my@gmail.com"
password = "abcdefg"

data = pandas.read_csv("birthdays.csv")
birth_dict = data.to_dict(orient="records")
target = {}
for info in birth_dict:
    if info["month"] == month and info["day"] == day:
        target = info
        new_letter = letters.replace("[NAME]", target["name"])
        subject = "Happy Birthday"
        body = new_letter
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = my_email
        msg["To"] = target["email"]

        smtp_server = "smtp.gmail.com"
        with smtplib.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(my_email, msg["To"], msg.as_string())
# print(target)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.









