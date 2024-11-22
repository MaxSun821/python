import smtplib
import requests
from datetime import datetime
from config import *


response = requests.get(url=ISS_API)
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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
time_now = datetime.now()

#If the ISS is close to my current position
if abs(MY_LAT - iss_latitude) + abs(MY_LONG - iss_longitude) <= 10:
    if time_now.hour > sunrise or time_now.hour < sunrise:
        pass


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



