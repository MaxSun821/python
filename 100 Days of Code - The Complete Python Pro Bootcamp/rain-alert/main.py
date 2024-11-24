import requests
from twilio.rest import Client
import os

OW_API = "https://api.openweathermap.org/data/2.5/forecast"
my_appid = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 29.031940,
    "lon": 111.678101,
    "appid": my_appid,
    "cnt": 4
}

response = requests.get(url=OW_API, params=weather_params)
will_rain = False
for item in response.json()["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages .create(
        body="Today will rain, please bring an umbrella🌧.",
        from_="",
        to=""
    )
    print(message.status)