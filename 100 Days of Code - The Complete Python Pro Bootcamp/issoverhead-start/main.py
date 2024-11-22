import smtplib
import time

import requests
from datetime import datetime
from config import *


#Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    response = requests.get(url=ISS_API)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(SUNRISE_API, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunrise or time_now <= sunset:
        return True

#If the ISS is close to my current position
while True:
    time.sleep(60)
    if iss_overhead() and is_dark():
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TARTGET_EMAIL,
                                msg="Subject:Iss Overhead\n\nLook Up now!!!"
                                )







