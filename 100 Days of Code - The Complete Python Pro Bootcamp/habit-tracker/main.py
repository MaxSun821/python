import requests
from config import *
# Create a user


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)