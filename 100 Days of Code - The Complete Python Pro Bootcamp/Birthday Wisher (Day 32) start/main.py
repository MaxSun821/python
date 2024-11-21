import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

my_email = "your's@gmail.com"
password = "abcdefg"

now = dt.datetime.now()
day_of_week = now.weekday()
with open("quotes.txt") as file:
    data_list = file.readlines()
if day_of_week == 3:
    subject = "Thursday's quote"
    body = random.choice(data_list)
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = my_email
    msg["To"] = "other's@outlook.com"

smtp_server = "smtp.gmail.com"

with smtplib.SMTP(smtp_server) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(msg["From"], msg["To"], msg.as_string())
