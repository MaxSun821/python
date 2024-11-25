from datetime import datetime
from config import *
import requests

response = requests.post(url=exercises_endpoint, json=exercises_parameters, headers=headers)
exercise_name = response.json()['exercises'][0]["name"]
exercise_duration = response.json()['exercises'][0]['duration_min']
nt_calories = response.json()['exercises'][0]['nf_calories']
today = datetime.now()
sheety_parameters = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_name.title(),
        "duration": exercise_duration,
        "calories": nt_calories
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters)