import requests
from twilio.rest import Client

OW_API = "https://api.openweathermap.org/data/2.5/forecast"
my_appid = "123"

account_sid = "123"
auth_token = "123"

weather_params = {
    "lat": 0,
    "lon": 0,
    "appid": my_appid,
    "cnt": 4
}

response = requests.get(url=OW_API, params=weather_params)
# print(response)
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

